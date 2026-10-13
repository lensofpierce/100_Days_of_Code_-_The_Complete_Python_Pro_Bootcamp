# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You did not provide valid inputs"
#
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"
#
#
# print(format_name(input("What is your first name?"), input("What is your last name?")))


# Coding Exercise 10: Leap Year
def is_leap_year(year):
    """Input a year and determine whether it is a leap year
    depending if it is divisible by 4, 100, or 400."""
    if int(year) % 4 == 0:
        if int(year) % 100 == 0:
            if int(year) % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(input("Is this a leap year? ")))
