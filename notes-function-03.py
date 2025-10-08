# function
# author : thierry n
# oct 8 2025


def say_hello():
    print("hello")

    say_hello()


# function to prin a personalized helloo
def say_hello_nicely(name: str):
    print(f"hello {name}!")

    say_hello_nicely("steve")


def normalize_input(user_input: str):
    """Takes user input and cleans it up."""
    output = user_input.lower().strip(",.?! ")
    return output


output = print(normalize_input("Rainy!"))

output = print(normalize_input("YES!!!!"))
