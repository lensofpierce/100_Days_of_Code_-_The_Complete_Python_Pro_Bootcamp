# # Modifying Global Scope
#
# enemies = 1
#
#
# def increase_enemies():
#     global enemies          # It is not recommended to modify global scopes, but you can at times
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Better method

enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


