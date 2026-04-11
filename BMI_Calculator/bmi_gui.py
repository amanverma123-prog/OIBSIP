import tkinter as tk

# Main Window
window = tk.Tk()
window.title("BMI_Calculator")
window.geometry("500x400")

# Title Label
title = tk.Label(window, text="BMI Calculator", font=("Arial", 20, "bold"))
title.pack(pady=20)

# User Input Parameters
weight_label = tk.Label(window, text="Enter your Weight (kg) : ",font=("Arial", 12))
weight_label.pack(pady=5)

# Input for Weight field
weight_entry = tk.Entry(window, font=("Arial", 12))
weight_entry.pack(pady=5)

# User Input for Height
height_label = tk.Label(window, text="Enter your Height (metres) : ",font=("Arial", 12))
height_label.pack(pady=5)

# Input for Hight field
height_entry = tk.Entry(window, font=("Arial", 12))
height_entry.pack(pady=5)

# Calculate Function
def calculate_bmi():
    try:
        # Taking Weight and Height as an Input from User
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Handling negative Inputs
        if weight <= 0 or height <= 0:
            result_label.config(text="Weight and Height must be a positive value!", fg="red")
            # Working Part
        else:
            # BMI Formula
            bmi = weight/(height**2)
            bmi = round(bmi, 2)

        # BMI Categories
        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif bmi >= 18.5 and bmi <= 24.9:
            category = "Normal"
            color = "green"
        elif bmi >= 25 and bmi <= 29.9:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"
        
        result_label.config(text=f"BMI : {bmi} - {category}", fg=color)

    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers only.", fg="red")

calc_button = tk.Button(window, text="Calculate BMI", font=("Arial", 12, "bold"), command=calculate_bmi)
calc_button.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=20)

# Main Window 
window.mainloop()