import tkinter as tk
from tkinter import ttk

from config import COLORS
from menu_ui.menu import init_menu
from books.book import init_book
from id_e.ide import init_ide
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.title("PyLearn IDE")
root.geometry("700x500")
root.configure(bg=COLORS["bg"])
root.iconbitmap(resource_path("assets/icon.ico"))

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Treeview",
    background=COLORS["tree_bg"],
    foreground=COLORS["tree_fg"],
    fieldbackground=COLORS["tree_bg"],
    borderwidth=0,
    font=("Segoe UI", 10),
)
style.map("Treeview", background=[("selected", COLORS["selection"])])

container = tk.Frame(root, bg=COLORS["bg"])
container.pack(fill="both", expand=True)

frames = {}


def create_frame(name):
    f = tk.Frame(container, bg=COLORS["bg"])
    f.place(relwidth=1, relheight=1)
    frames[name] = f
    return f


def show(name):
    frames[name].tkraise()


init_menu(create_frame, show)
init_book(create_frame, show)
init_ide(create_frame, show, root)

show("menu")
root.mainloop()
