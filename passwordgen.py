import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", f"Error: {ve}")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))

    label_result.config(text=f"Generated Password: {password}")


window = tk.Tk()
window.title("Password Generator")
window.configure(background="black")
window.resizable(False,False)

label_length = tk.Label(window, text="Enter password length:", font=("Arial", 14), bg="black", fg="white")
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(window, font=("Arial", 14))
entry_length.grid(row=0, column=1, padx=10, pady=10)

button_generate = tk.Button(window, text="Generate Password", font=("Arial", 14), command=generate_password, bg="yellow", fg="red")
button_generate.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(window, text="", font=("Arial", 14), bg="black", fg="white", wraplength=300)
label_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


window.mainloop()
