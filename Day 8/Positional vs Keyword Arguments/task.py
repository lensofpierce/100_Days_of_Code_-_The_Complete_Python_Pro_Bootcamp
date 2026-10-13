# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with("Jack Bauer", "Nowhere")

greet_with(location = "Nowhere", name = "Jack Bauer")


# Coding Exercise 8: Love Calculator
def calculate_love_score(name1, name2):
    t_count = name1.lower().count("t") + name2.lower().count("t")
    r_count = name1.lower().count("r") + name2.lower().count("r")
    u_count = name1.lower().count("u") + name2.lower().count("u")
    e_count = name1.lower().count("e") + name2.lower().count("e")
    true_count = t_count + r_count + u_count + e_count
    print(t_count)
    print(r_count)
    print(u_count)
    print(e_count)
    print(true_count)

    l_count = name1.lower().count("l") + name2.lower().count("l")
    o_count = name1.lower().count("o") + name2.lower().count("o")
    v_count = name1.lower().count("v") + name2.lower().count("v")
    e_count = name1.lower().count("e") + name2.lower().count("e")
    love_count = l_count + o_count + v_count + e_count
    print(l_count)
    print(o_count)
    print(v_count)
    print(e_count)
    print(love_count)

    love_score = int(str(true_count) + str(love_count))
    print(love_score)

calculate_love_score("Kanye West", "Kim Kardashian")