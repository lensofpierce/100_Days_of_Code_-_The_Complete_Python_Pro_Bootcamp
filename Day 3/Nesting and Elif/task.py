print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:                    # elif age <= 12: (from Dr. Yu)
        print("Please pay $5.00.")
    elif 12 <= age <= 18:           # elif age <=18: (from Dr. Yu)
        print("Please pay $7.00")
    else:
        print("You're old. Pay $12.00. :P")
else:
    print("Sorry you have to grow taller before you can ride.")
