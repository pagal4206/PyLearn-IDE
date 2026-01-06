import tkinter as tk
from syn.syntax import apply_coloring
from config import COLORS, FONT_CODE, FONT_UI
from menu_ui.button import HoverButton
from books.lesson import lessons


def init_book(create_frame, show):
    book = create_frame("book")

    book_head = tk.Frame(book, bg=COLORS["sidebar"], height=50)
    book_head.pack(fill="x")

    HoverButton(
        book_head,
        text="⬅ Back",
        bg=COLORS["sidebar"],
        fg="white",
        command=lambda: show("menu"),
    ).pack(side="left", padx=10, pady=10)

    tk.Label(
        book_head,
        text="📚 Python Book",
        bg=COLORS["sidebar"],
        fg="white",
        font=FONT_UI,
    ).pack(side="left")

    book_pane = tk.PanedWindow(
        book, orient="horizontal", bg=COLORS["bg"], sashwidth=4, sashrelief="flat"
    )
    book_pane.pack(fill="both", expand=True, padx=10, pady=10)

    lb = tk.Listbox(
        book_pane,
        font=FONT_UI,
        bg=COLORS["sidebar"],
        fg="white",
        borderwidth=0,
        selectbackground=COLORS["selection"],
    )
    book_pane.add(lb, width=200)

    book_view = tk.Text(
        book_pane,
        font=FONT_CODE,
        bg=COLORS["bg"],
        fg=COLORS["text"],
        borderwidth=0,
        padx=10,
        pady=10,
        state="disabled",
    )
    book_pane.add(book_view)

    for t in lessons:
        lb.insert(tk.END, t)

    def load_topic(e):
        if not lb.curselection():
            return
        val = lessons[lb.get(lb.curselection())]
        book_view.config(state="normal")
        book_view.delete("1.0", tk.END)
        book_view.insert("1.0", val)
        apply_coloring(book_view)
        book_view.config(state="disabled")

    lb.bind("<<ListboxSelect>>", load_topic)

