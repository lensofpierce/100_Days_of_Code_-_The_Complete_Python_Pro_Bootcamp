import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# # Easy Version
# password_chars = []
# for i in range(nr_letters):
#     password_chars.append(random.choice(letters))
# for i in range(nr_symbols):
#     password_chars.append(random.choice(symbols))
# for i in range(nr_numbers):
#     password_chars.append(random.choice(numbers))
#
# num_characters = nr_letters + nr_symbols + nr_numbers
# print("The number of characters in your password are: " + str(num_characters))
# print(password_chars)
# password = "".join(password_chars)
# print(password)

# Hard Version
password_chars = []
for i in range(nr_letters):
    password_chars.append(random.choice(letters))
for i in range(nr_symbols):
    password_chars.append(random.choice(symbols))
for i in range(nr_numbers):
    password_chars.append(random.choice(numbers))

num_characters = nr_letters + nr_symbols + nr_numbers
print("The number of characters in your password are: " + str(num_characters))
print("Selected Characters: ")
print(password_chars)
random.shuffle(password_chars)
print("Shuffling for better protection...")
print(password_chars)
password = "".join(password_chars)
print(f"\nYour new password is: {password}")

