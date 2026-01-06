import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
import sys, re, os, threading, ctypes, time

from syn.syntax import apply_coloring
from config import COLORS, FONT_CODE
from menu_ui.button import HoverButton


def init_ide(create_frame, show, root):
    execution_thread = None
    current_file_path = None
    current_project_path = None

    ide = create_frame("ide")

    toolbar = tk.Frame(ide, bg=COLORS["sidebar"], height=45)
    toolbar.pack(fill="x", side="top")

    HoverButton(
        toolbar,
        text="⬅",
        width=4,
        bg=COLORS["sidebar"],
        fg="white",
        command=lambda: show("menu"),
    ).pack(side="left")

    tk.Label(toolbar, text=" | ", bg=COLORS["sidebar"], fg="gray").pack(side="left")

    layout_pane = tk.PanedWindow(ide, orient="horizontal", bg=COLORS["bg"], sashwidth=4)
    layout_pane.pack(fill="both", expand=True)

    sidebar_frame = tk.Frame(layout_pane, bg=COLORS["sidebar"])
    layout_pane.add(sidebar_frame, width=250)

    tk.Label(
        sidebar_frame,
        text=" EXPLORER",
        bg=COLORS["sidebar"],
        fg="gray",
        font=("Segoe UI", 9, "bold"),
    ).pack(anchor="w", padx=5, pady=5)

    file_tree = ttk.Treeview(sidebar_frame, show="tree", selectmode="browse")
    file_tree.pack(fill="both", expand=True, padx=5, pady=5)

    file_tree_scroll = ttk.Scrollbar(
        sidebar_frame, orient="vertical", command=file_tree.yview
    )
    file_tree_scroll.place(relx=1.0, rely=0, relheight=1, anchor="ne")
    file_tree.configure(yscrollcommand=file_tree_scroll.set)

    main_pane = tk.PanedWindow(
        layout_pane, orient="vertical", bg=COLORS["bg"], sashwidth=4
    )
    layout_pane.add(main_pane)

    editor_frame = tk.Frame(main_pane, bg=COLORS["bg"])
    main_pane.add(editor_frame, height=500)

    line_nums = tk.Text(
        editor_frame,
        width=4,
        bg=COLORS["bg"],
        fg=COLORS["line_num_fg"],
        font=FONT_CODE,
        state="disabled",
        padx=5,
        pady=10,
    )
    line_nums.pack(side="left", fill="y")

    editor = tk.Text(
        editor_frame,
        font=FONT_CODE,
        bg=COLORS["bg"],
        fg=COLORS["text"],
        insertbackground="white",
        undo=True,
        padx=10,
        pady=10,
        borderwidth=0,
    )
    editor.pack(side="left", fill="both", expand=True)

    output_frame = tk.Frame(main_pane, bg="#111111")
    main_pane.add(output_frame)

    tk.Label(
        output_frame,
        text=" TERMINAL",
        bg="#111111",
        fg="gray",
        font=("Segoe UI", 9, "bold"),
    ).pack(anchor="w", padx=5, pady=2)

    output = tk.Text(
        output_frame,
        bg="#111111",
        fg="#cccccc",
        font=("Consolas", 11),
        padx=10,
        pady=5,
        borderwidth=0,
    )
    output.pack(fill="both", expand=True)

    status_bar = tk.Label(
        ide,
        text=" Ready",
        bg=COLORS["accent"],
        fg="white",
        anchor="w",
        font=("Segoe UI", 9),
    )
    status_bar.pack(fill="x", side="bottom")

    class RealTimeRedirector:
        def __init__(self, widget):
            self.widget = widget

        def write(self, s):
            self.widget.after(0, lambda: self._append(s))

        def _append(self, s):
            self.widget.insert(tk.END, s)
            self.widget.see(tk.END)

        def flush(self):
            pass

    def custom_input(prompt=""):
        return simpledialog.askstring("Input", prompt, parent=root) or ""

    def update_editor(event=None):
        lines = editor.get("1.0", tk.END).count("\n")
        line_nums.config(state="normal")
        line_nums.delete("1.0", tk.END)
        line_nums.insert("1.0", "\n".join(str(i) for i in range(1, lines + 2)))
        line_nums.config(state="disabled")
        line_nums.yview_moveto(editor.yview()[0])
        apply_coloring(editor)

        pos = editor.index(tk.INSERT).split(".")
        fname = os.path.basename(current_file_path) if current_file_path else "Untitled"
        status_bar.config(
            text=f" {fname} | Ln {pos[0]}, Col {int(pos[1])+1} | Python 3"
        )

    def auto_indent(event):
        line = editor.get("insert linestart", "insert lineend")
        indent = re.match(r"\s*", line).group()
        if line.strip().endswith(":"):
            indent += "    "
        editor.insert(tk.INSERT, "\n" + indent)
        return "break"

    def format_code():
        code = editor.get("1.0", tk.END).splitlines()
        formatted, indent = [], 0
        for line in code:
            stripped = line.strip()
            if not stripped:
                formatted.append("")
                continue
            if stripped.startswith(("return", "break", "continue", "pass")):
                indent = max(indent - 1, 0)
            formatted.append("    " * indent + stripped)
            if stripped.endswith(":"):
                indent += 1
        editor.delete("1.0", tk.END)
        editor.insert("1.0", "\n".join(formatted))
        update_editor()

    def new_file():
        nonlocal current_file_path
        current_file_path = None
        editor.delete("1.0", tk.END)
        update_editor()

    def open_file():
        nonlocal current_file_path
        path = filedialog.askopenfilename(
            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if path:
            load_content(path)

    def save_file():
        nonlocal current_file_path
        if current_file_path:
            with open(current_file_path, "w", encoding="utf-8") as f:
                f.write(editor.get("1.0", tk.END))
        else:
            path = filedialog.asksaveasfilename(
                defaultextension=".py", filetypes=[("Python Files", "*.py")]
            )
            if path:
                current_file_path = path
                save_file()

    def load_content(path):
        nonlocal current_file_path
        with open(path, "r", encoding="utf-8") as f:
            editor.delete("1.0", tk.END)
            editor.insert("1.0", f.read())
        current_file_path = path
        update_editor()

    def open_folder():
        nonlocal current_project_path
        folder = filedialog.askdirectory()
        if not folder:
            return
        current_project_path = folder
        file_tree.delete(*file_tree.get_children())

        def populate(path, parent=""):
            for item in sorted(os.listdir(path)):
                full = os.path.join(path, item)
                node = file_tree.insert(parent, "end", text=item, values=[full])
                if os.path.isdir(full):
                    populate(full, node)

        populate(folder)

    def on_tree_click(event):
        item = file_tree.selection()
        if not item:
            return
        path = file_tree.item(item[0], "values")
        if path and os.path.isfile(path[0]):
            load_content(path[0])

    file_tree.bind("<Double-1>", on_tree_click)

    def run_code():
        nonlocal execution_thread
        if execution_thread and execution_thread.is_alive():
            return

        output.delete("1.0", tk.END)

        def execute():
            old = sys.stdout
            sys.stdout = RealTimeRedirector(output)
            try:
                exec(
                    editor.get("1.0", tk.END),
                    {"input": custom_input, "time": time, "os": os, "sys": sys},
                )
            except Exception as e:
                error_msg = str(e)
                print(error_msg)
                root.after(0, lambda: jump_to_error_line(error_msg))
            finally:
                sys.stdout = old

        execution_thread = threading.Thread(target=execute, daemon=True)
        execution_thread.start()

    def stop_code():
        nonlocal execution_thread
        if execution_thread and execution_thread.is_alive():
            ctypes.pythonapi.PyThreadState_SetAsyncExc(
                execution_thread.ident, ctypes.py_object(SystemExit)
            )
            output.insert(tk.END, "\n[Stopped]\n")

    def clear_output():
        output.delete("1.0", tk.END)

    def jump_to_error_line(err):
        match = re.search(r"line (\d+)", err)
        if not match:
            return

        line_no = int(match.group(1))

        editor.mark_set("insert", f"{line_no}.0")
        editor.see(f"{line_no}.0")

        editor.tag_remove("error_line", "1.0", tk.END)
        editor.tag_add("error_line", f"{line_no}.0", f"{line_no}.end")
        editor.tag_config("error_line", background="#51202A")

    HoverButton(
        toolbar, text="📄 New", bg=COLORS["sidebar"], fg="white", command=new_file
    ).pack(side="left", padx=2)
    HoverButton(
        toolbar, text="📂 Open", bg=COLORS["sidebar"], fg="white", command=open_file
    ).pack(side="left", padx=2)
    HoverButton(
        toolbar, text="📁 Folder", bg=COLORS["sidebar"], fg="white", command=open_folder
    ).pack(side="left", padx=2)
    HoverButton(
        toolbar, text="💾 Save", bg=COLORS["sidebar"], fg="white", command=save_file
    ).pack(side="left", padx=2)
    HoverButton(
        toolbar, text="🧹 Format", bg=COLORS["sidebar"], fg="white", command=format_code
    ).pack(side="left", padx=2)

    HoverButton(
        toolbar, text="🧹 Clear", bg=COLORS["sidebar"], fg="white", command=clear_output
    ).pack(side="right", padx=10)
    HoverButton(
        toolbar, text="⏹ Stop", bg=COLORS["danger"], fg="white", command=stop_code
    ).pack(side="right", padx=5)
    HoverButton(
        toolbar, text="▶ Run", bg=COLORS["success"], fg="white", command=run_code
    ).pack(side="right", padx=5)

    editor.bind("<KeyRelease>", update_editor)
    editor.bind("<MouseWheel>", update_editor)
    editor.bind("<Button-1>", update_editor)
    editor.bind("<Tab>", lambda e: editor.insert(tk.INSERT, "    ") or "break")
    editor.bind("<Return>", auto_indent)

    editor.insert("1.0", "print('Hello World')")
    update_editor()
