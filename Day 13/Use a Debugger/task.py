import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])



# # Coding Exercise 12: Debugging Odd or Even
# def odd_or_even(number):
#     # Bug: It should be == instead of =
#     if number % 2 == 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."
#
#
# number_result = odd_or_even(int(input("Enter a number: ")))
# print(number_result)


# # Coding Exercise 13: Debugging Leap Year
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             # Should be 400 instead of 4000
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# leap_or_not = is_leap(int(input("Input year: ")))
# print(leap_or_not)


# # Coding Exercise 14: Debugging FizzBuzz
# # Target is the number up to which we count
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         # use and (not or)
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         # use elif (not if)
#         elif number % 3 == 0:
#             print("Fizz")
#         # use elif (not if)
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             # remove square brackets []
#             print(number)
#
#
# max_fizz_buzz = fizz_buzz(int(input("Input the target number: ")))