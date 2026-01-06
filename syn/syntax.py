import re
import tkinter as tk


def apply_coloring(text_widget):
    content = text_widget.get("1.0", tk.END)
    for tag in ["kwd", "str", "cmt", "blt", "num"]:
        text_widget.tag_remove(tag, "1.0", tk.END)

    patterns = [
        (
            r"\b(def|class|if|else|elif|for|while|return|import|from|break|continue|pass|in|is|and|or|not|with|as|global|try|except|finally)\b",
            "kwd",
            "#c586c0",
        ),
        (
            r"\b(print|input|len|range|int|str|float|bool|list|tuple|set|dict|type|open|id|os|sys)\b",
            "blt",
            "#dcdcaa",
        ),
        (r"'.*?'|\".*?\"", "str", "#ce9178"),
        (r"#.*", "cmt", "#6a9955"),
        (r"\b\d+\b", "num", "#b5cea8"),
    ]

    for pat, tag, color in patterns:
        text_widget.tag_config(tag, foreground=color)
        for match in re.finditer(pat, content):
            text_widget.tag_add(
                tag, f"1.0 + {match.start()} chars", f"1.0 + {match.end()} chars"
            )
