# Prompt the user for their age until they provide a valid input
while True:
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Age cannot be negative. Please try again.")
            continue  # Continue to prompt for input
        else:
            break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("Thank you for providing your age:", age)
