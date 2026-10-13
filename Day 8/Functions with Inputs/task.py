# def greet():
#     print("Hello Angela")
#     print("How do you do Jack Bauer?")
#     print("Isn't the weather nice?")
#
# greet()

Functions that allows for inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice?")

greet_with_name("Billie")


# Coding Exercise 7
age = input("How old are you? ")
def life_in_weeks(age):
    x = (90 - int(age)) * 52
    print(f"You have {x} weeks left.")

life_in_weeks(age)