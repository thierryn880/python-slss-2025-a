# choose your own adventure
# Thierry Narcisse
# 24 september

# choose your own adventure focusing on using variables and braching/conditionals

# introducton

# problem

# Rising action

# climax

# resolution

greeting = "hello player, welcome to the best adventure game!"

user_name = input(" what is your name...player?")

print(f"it's nice to meet you, {user_name}.")

print(
    "this will be an adventure throughout the deep forests from the land of CARL.....but we have a problem "
)


print("There is a monster lurking  around in the forest and we want you to fight it..")

print("so do you want to help us fight this monster?")

choice_path = input()

if choice_path == "yes":
    print(f"Hurry up before the monster finds us {user_name} ")

    print("You pick up your gear: a sword and a MR.UBIAL shield.")

    print("As you enter the forest, you see two paths open before you.")

    print("Do you want to go 'left' toward the river or 'right' toward the dark cave?")

elif choice_path == "no":
    print("ok bye then")

else:
    print("secret message")

path_yap = input()


if path_yap == "left":
    print("You follow the river, and it's quiet... too quiet.")

    print("Suddenly, a giant serpent rises from the water!")

else:
    print(
        "you go right and hit a dead end. You decide to not help the land of CARL and go to mcdonalds"
    )
