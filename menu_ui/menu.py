import tkinter as tk
import webbrowser
from config import COLORS, GITHUB_REPO
from menu_ui.button import HoverButton


def init_menu(create_frame, show):
    menu = create_frame("menu")

    card = tk.Frame(menu, bg=COLORS["sidebar"], padx=40, pady=40)
    card.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        card,
        text="PyLearn IDE",
        font=("Segoe UI", 28, "bold"),
        bg=COLORS["sidebar"],
        fg=COLORS["accent"],
    ).pack(pady=(0, 10))

    tk.Label(
        card,
        text="GPC JODHPUR",
        font=("Segoe UI", 12),
        bg=COLORS["sidebar"],
        fg="gray",
    ).pack(pady=(0, 30))

    HoverButton(
        card,
        text="📘 Open Lessons",
        font=("Segoe UI", 14),
        width=20,
        pady=5,
        bg=COLORS["line_num_bg"],
        fg="white",
        hover_bg="#3c3c3c",
        command=lambda: show("book"),
    ).pack(pady=10)

    HoverButton(
        card,
        text="💻 Start Coding",
        font=("Segoe UI", 14),
        width=20,
        pady=5,
        bg=COLORS["accent"],
        fg="white",
        hover_bg=COLORS["accent_hover"],
        command=lambda: show("ide"),
    ).pack(pady=10)

    link = tk.Label(
        menu,
        text="Get Source Code on GitHub 🔗",
        bg=COLORS["bg"],
        fg="#569cd6",
        cursor="hand2",
    )
    link.place(relx=0.5, rely=0.95, anchor="center")
    link.bind("<Button-1>", lambda e: webbrowser.open(GITHUB_REPO))
