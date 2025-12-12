# Modifying Global Scope

enemies = "skeleton"


def increase_enemies():
    enemies = "zombie"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


