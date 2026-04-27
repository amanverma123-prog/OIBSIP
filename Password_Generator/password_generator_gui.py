import tkinter as tk
import string
import random

# Main Window
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x400")

# Title Label
title = tk.Label(window, text="Password Generator", font=("Arial", 20, "bold"))
title.pack(pady=20)

# User Input Parameters
length_label = tk.Label(window, text="Enter the length of password : ",font=("Arial", 12))
length_label.pack(pady=5)

# Entry of Input
length_entry = tk.Entry(window, font=("Arial", 12))
length_entry.pack(pady=5)

# CheckBox Variables
var_letters = tk.IntVar()
var_numbers = tk.IntVar()
var_symbols = tk.IntVar()

# CheckBoxes
letters_check = tk.Checkbutton(window, text= "Include Letters",font=("Arial", 12), variable=var_letters)
letters_check.pack(anchor="w", padx=150, pady=5)
numbers_check = tk.Checkbutton(window, text= "Include Numbers",font=("Arial", 12), variable=var_numbers)
numbers_check.pack(anchor="w", padx=150, pady=5)
symbols_check = tk.Checkbutton(window, text= "Include Symbols",font=("Arial", 12), variable=var_symbols)
symbols_check.pack(anchor="w", padx=150, pady=5)

# Password Generator Function
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Length must be greater than 0!", fg="red")
        else:
            characters = ""
            if var_letters.get() == 1:
                characters += string.ascii_letters
            if var_numbers.get() == 1:
                characters += string.digits
            if var_symbols.get() == 1:
                characters += string.punctuation
            
            if characters == "":
                result_label.config(text="Please select at least one option!", fg="red")
            else:
                password = ""
                for i in range(length):
                    password += random.choice(characters)
                
                result_label.config(text=f"Password: {password}", fg="green")
    
    except ValueError:
        result_label.config(text="Invalid input! Enter a number.", fg="red")
        
# Result Label
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=20)

# Generate Button
generate_button = tk.Button(window, text="Generate Password", font=("Arial", 12, "bold"), command=generate_password)
generate_button.pack(pady=20)

window.mainloop()