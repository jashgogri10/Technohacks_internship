import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    characters = ""
    
    if use_letters.get():
        characters += string.ascii_letters
    if use_digits.get():
        characters += string.digits
    if use_punctuation.get():
        characters += string.punctuation
    
    if strength_var.get() == "weak":
        characters = string.ascii_letters
        
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text="Generated Password: " + generated_password)

# Create the main window
root = tk.Tk()
root.geometry("500x500")
root.title("Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

use_letters = tk.IntVar()
use_digits = tk.IntVar()
use_punctuation = tk.IntVar()

letters_checkbox = tk.Checkbutton(root, text="Use Letters", variable=use_letters)
letters_checkbox.pack()

digits_checkbox = tk.Checkbutton(root, text="Use Digits", variable=use_digits)
digits_checkbox.pack()

punctuation_checkbox = tk.Checkbutton(root, text="Use Punctuation", variable=use_punctuation)
punctuation_checkbox.pack()

strength_var = tk.StringVar()
strength_label = tk.Label(root, text="Select Password Strength:")
strength_label.pack()

strength_weak = tk.Radiobutton(root, text="Weak", variable=strength_var, value="weak")
strength_weak.pack()

strength_average = tk.Radiobutton(root, text="Average", variable=strength_var, value="average")
strength_average.pack()

strength_strong = tk.Radiobutton(root, text="Strong", variable=strength_var, value="strong")
strength_strong.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

# Start the GUI event loop
root.mainloop()