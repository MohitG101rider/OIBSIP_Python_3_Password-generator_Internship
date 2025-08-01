import tkinter as tk
from tkinter import ttk
import string
import random
import pyperclip

#logic
def generate_password():
    length = length_slider.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = number_var.get()
    use_symbols = symbol_var.get()

    chars = ""
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation

    if not chars:
        password_var.set("Select options")
        strength_label.config(text="Strength: ❌")
        return

    password = "".join(random.choice(chars) for _ in range(int(length)))
    password_var.set(password)
    evaluate_strength(password)

def copy_password():
    pyperclip.copy(password_var.get())
    copy_button.config(text="✅ Copied!")
    root.after(1500, lambda: copy_button.config(text="📋 Copy"))

def evaluate_strength(pwd):
    strength = 0
    if any(c.islower() for c in pwd): strength += 1
    if any(c.isupper() for c in pwd): strength += 1
    if any(c.isdigit() for c in pwd): strength += 1
    if any(c in string.punctuation for c in pwd): strength += 1

    if len(pwd) >= 12 and strength >= 3:
        strength_label.config(text="Strength: 🔒 Strong", foreground="#10b981")
    elif len(pwd) >= 8 and strength >= 2:
        strength_label.config(text="Strength: 🟡 Medium", foreground="#fbbf24")
    else:
        strength_label.config(text="Strength: 🔴 Weak", foreground="#ef4444")

#gui
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("480x460")
root.config(bg="#0f172a")
root.resizable(False, False)

style = ttk.Style()
style.configure("TCheckbutton", background="#0f172a", foreground="#f1f5f9", font=("Segoe UI", 10))
style.configure("TLabel", background="#0f172a", foreground="#f1f5f9")
style.configure("TButton", font=("Segoe UI", 10, "bold"))

title = ttk.Label(root, text="✨ Futuristic Password Generator", font=("Segoe UI", 14, "bold"))
title.pack(pady=20)

#frame
output_frame = tk.Frame(root, bg="#1e293b", bd=2, relief="sunken")
output_frame.pack(padx=20, pady=10, fill="x")

password_var = tk.StringVar()
password_entry = tk.Entry(output_frame, textvariable=password_var, font=("Consolas", 14), bd=0,
                          bg="#f1f5f9", fg="#0f172a")
password_entry.pack(side="left", fill="x", expand=True, padx=(5, 0), ipady=6)

copy_button = tk.Button(output_frame, text="📋 Copy", command=copy_password, bg="#4f46e5",
                        fg="white", font=("Segoe UI", 10), activebackground="#6366f1")
copy_button.pack(side="right", padx=5, pady=4)

#set
settings_frame = tk.Frame(root, bg="#0f172a")
settings_frame.pack(padx=20, pady=15, fill="x")

length_label = ttk.Label(settings_frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky="w")

length_slider = ttk.Scale(settings_frame, from_=6, to=30, orient="horizontal")
length_slider.set(12)
length_slider.grid(row=0, column=1, sticky="ew", padx=10)
settings_frame.columnconfigure(1, weight=1)

#conditions
check_frame = tk.Frame(root, bg="#0f172a")
check_frame.pack(padx=20, pady=10, fill="x")

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=False)

ttk.Checkbutton(check_frame, text="Include Uppercase (A-Z)", variable=upper_var).pack(anchor="w")
ttk.Checkbutton(check_frame, text="Include Lowercase (a-z)", variable=lower_var).pack(anchor="w")
ttk.Checkbutton(check_frame, text="Include Numbers (0-9)", variable=number_var).pack(anchor="w")
ttk.Checkbutton(check_frame, text="Include Symbols (!@#$...)", variable=symbol_var).pack(anchor="w")

#button
generate_button = tk.Button(root, text="🔄 Generate Password", command=generate_password,
                            bg="#10b981", fg="white", font=("Segoe UI", 11, "bold"),
                            activebackground="#059669")
generate_button.pack(pady=15, ipadx=10, ipady=5)

#display strength
strength_label = ttk.Label(root, text="Strength: Medium", font=("Segoe UI", 10, "bold"))
strength_label.pack()

root.mainloop()
