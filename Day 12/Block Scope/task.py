# There is no block scope in python

game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()



# Coding Exercise 11: Prime Number Checker
def is_prime(num):
    if num < 2:
        return False

    # Loop through all the numbers between 2 and the number
    for number in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % number == 0:
            return False
    # This return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore, it is prime.
    return True

check_number = int(input("Input a number to be checked as a prime: "))
print(is_prime(check_number))