import tkinter as tk
from tkinter import ttk

# ==================== WINDOW SETUP ====================
window = tk.Tk()
window.title("FNgyCalculator")
window.geometry("350x500")
window.resizable(False, False)
window.config(bg="#1e1e1e")

# ==================== STYLING ====================
style = ttk.Style()
style.theme_use("clam")  # Modern theme for better colors

# Base style for all buttons (dark gray by default)
style.configure(
    "Rounded.TButton",
    font=("DejaVu Sans", 16),
    foreground="white",
    background="#333333",
    borderwidth=0,
    relief="flat",
    padding=10
)

# Number buttons (slightly lighter gray)
style.configure(
    "Number.TButton", 
    font=("DejaVu Sans", 16), 
    borderwidth=0, 
    foreground="white", 
    background="#4d4d4d"
)
style.map("Number.TButton", background=[("active", "#666666")])

# Equals button (light blue)
style.configure(
    "Equal.TButton", 
    font=("DejaVu Sans", 16), 
    borderwidth=0, 
    foreground="white", 
    background="#267ed6"
)
style.map("Equal.TButton", background=[("active", "#2a8fd3")])

# ==================== DISPLAYS ====================
inMemory = tk.Label(
    window, text="", font=("DejaVu Sans", 12),
    fg="#888888", bg="#1e1e1e", anchor="e"
)
inMemory.grid(row=0, column=0, columnspan=4, sticky="we", padx=5, pady=(5,0))

withCurrent = tk.Label(
    window, text="0", font=("DejaVu Sans", 28),
    fg="white", bg="#1e1e1e", anchor="e"
)
withCurrent.grid(row=1, column=0, columnspan=4, sticky="we", padx=5, pady=(0,10))

# ==================== BUTTON LAYOUT ====================
buttons = [
    ["%", "CE", "C", "⌫"],
    ["1/x", "x²", "√", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="]
]

# ==================== CREATE BUTTONS ====================
for r, row in enumerate(buttons):
    for c, b in enumerate(row):
        # Decide button style
        if b in "0123456789":
            btn_style = "Number.TButton"
        elif b == "=":
            btn_style = "Equal.TButton"
        else:
            btn_style = "Rounded.TButton"
        # Create button (no functionality yet)
        btn = ttk.Button(window, text=b, style=btn_style, command=lambda: None)
        btn.grid(row=r+2, column=c, sticky="nsew", padx=2, pady=2)

# ==================== MAKE GRID RESIZABLE ====================
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(2, 8):  # rows for buttons
    window.grid_rowconfigure(i, weight=1)

# ==================== RUN APP ====================
window.mainloop()
