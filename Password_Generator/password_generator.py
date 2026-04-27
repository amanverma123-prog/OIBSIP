import random
import string

try:
    length = int(input("Enter the length of the password : "))
    
    # If negative length passed
    if length <= 0:
        print("Password length must be greater than 0!")
    else:
        use_letters = input("Do you want to use letters in your password(y/n): ")
        use_numbers = input("Do you want to use numbers in your password(y/n): ")
        use_symbols = input("Do you want to use symbols in your password(y/n): ")

        # Character pool
        characters = ""

        if use_letters == 'y':
            characters += string.ascii_letters
        if use_numbers == 'y':
            characters += string.digits
        if use_symbols == 'y':
            characters += string.punctuation
        if characters == "":
            print("Please select the type of password!")
        else:
            password = ""
            for i in range(length):
                password += random.choice(characters)
            
            print(f"Your password is: {password}")

except ValueError:
    # If something like (abc) passed
    print("Invalid input! Please enter a number for length.")