import tkinter as tk

from config import COLORS


class HoverButton(tk.Button):
    """A Button that changes color on hover"""

    def __init__(self, master, **kwargs):
        self.default_bg = kwargs.get("bg", COLORS["sidebar"])
        self.hover_bg = kwargs.pop("hover_bg", COLORS["accent"])

        kwargs["relief"] = tk.FLAT
        kwargs["borderwidth"] = 0
        kwargs["cursor"] = "hand2"
        kwargs["activebackground"] = self.hover_bg
        kwargs["activeforeground"] = "white"

        super().__init__(master, **kwargs)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.config(bg=self.hover_bg)

    def on_leave(self, e):
        self.config(bg=self.default_bg)
