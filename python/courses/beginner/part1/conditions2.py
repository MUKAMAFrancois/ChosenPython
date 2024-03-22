# grading system
mark = int(input("Enter your mark: "))

def decision(mark):
    if mark > 90:
        return "A"
    elif 80 < mark <= 90:
        return "B"
    elif 70 < mark <= 80:
        return "C"
    elif 60 < mark <= 70:
        return "D"
    else:
        return "F"

print(f"Your grade is: {decision(mark)}")



# BMI Calculator

height = float(input("Enter your Height in m: "))
weight = float(input("Enter your Weight in kg: "))

bmi = weight / (height ** 2)

def decision(value):
    if value < 18.5:
        return "You are underweight!"
    elif 18.5 <= value < 25:
        return "Your weight is normal."
    elif 25 <= value < 30:
        return "You are overweight."
    else:
        return "You are obese."
        
formated_bmi= "{:.3f}".format(bmi)

print(f"Result from BMI Calculator: {decision(bmi)} And your BMI is: {formated_bmi}")


# Calendar acts

calendar = {
    "Monday": ["Meeting with team", "Gym at 6 PM"],
    "Tuesday": ["Doctor's appointment", "Dinner with friends"],
    "Wednesday": ["Project presentation", "Movie night"],
    "Thursday": ["Lunch with client", "Networking event"],
    "Friday": ["Conference call", "Birthday party"],
    "Saturday": ["Shopping", "Family picnic"],
    "Sunday": ["Brunch with family", "Relaxing at home"]
}


for day, events in calendar.items():
    print(f"Events on {day}:")
    for event in events:
        print(f"  - {event}")


""" 
Events on Monday:
  - Meeting with team
  - Gym at 6 PM
Events on Tuesday:
  - Doctor's appointment
  - Dinner with friends
Events on Wednesday:
  - Project presentation
  - Movie night
Events on Thursday:
  - Lunch with client
  - Networking event
Events on Friday:
  - Conference call
  - Birthday party
Events on Saturday:
  - Shopping
  - Family picnic
Events on Sunday:
  - Brunch with family
  - Relaxing at home
 """


# Prompt the user for their age until they provide a valid input
while True:
    try:
        age = int(input("Please enter your age: "))
        if age <=0:
            print("Age cannot be negative. Please try again.")
            continue  # Continue to prompt for input
        else:
            break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("Thank you for providing your age:", age)
