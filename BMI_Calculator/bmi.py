try:
    # Taking Weight and Height as an Input from User
    weight = float(input("Enter your weight in kg : "))
    height = float(input("Enter your height in metres : "))

    # Handling negative Inputs
    if weight <= 0 or height <= 0:
        print("Weight and Height must be a positive value!")
        # Working Part
    else:
        # BMI Formula
        bmi = weight/(height**2)

        print(f"Your BMI is : {round(bmi, 2)}")

        # BMI Categories
        if bmi < 18.5:
            print("You are Underweight!")
        elif bmi >= 18.5 and bmi <= 24.9:
            print("You are Normal!")
        elif bmi >= 25 and bmi <= 29.9:
            print("You are Overweight!")
        else:
            print("You are Obese!")

except ValueError:
    print("Invalid input! Please enter numbers only.")