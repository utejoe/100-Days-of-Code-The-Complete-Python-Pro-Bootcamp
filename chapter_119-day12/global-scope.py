enemies = 1

def increase_enemies():
    # This creates a new local variable 'enemies' instead of modifying the global one
    enemies = 2
    print(f"Local enemies: {enemies}")  # This prints "2"

increase_enemies()
print(f"Global enemies: {enemies}")  # This prints "1"

# To modify the global variable, declare it as global within the function
def increase_global_enemies():
    global enemies
    enemies += 1

increase_global_enemies()
print(f"Modified global enemies: {enemies}")  # This prints "2"

# Alternatively, use return statements to modify global variables indirectly
def increase_enemies_return(enemies):
    return enemies + 1

enemies = increase_enemies_return(enemies)
print(f"Modified global enemies using return: {enemies}")  # This prints "3"
