def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? It loops based on i which goes from 1 to 19
# 2. When is the function meant to print "You got it"? When i is 20, but the range goes up to 19 only
# 3. What are your assumptions about the value of i? It won't print anything because the range does not cover 20
