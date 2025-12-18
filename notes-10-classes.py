# classes and objects
# Thierry N
# dec 11 2025

import random
from ctypes import c_buffer


class Pokemon:
    def __init__(self):
        self.name = "Pikachu"
        self.species = "Pikachu"
        self.type = "Electric"
        self.dance = 0
        self.age = 0
        self.level = 1
        print(f"{self.name} is born !")
        if random.randint(0, 4096):
            self.shiny = False
        else:
            self.shiny = True
            print(f"{self.name} is shiny!")

    def talk(self):
        """here what the pokemon has to say. The pokemon says its species name."""
        print(f'{self.name} says, "{self.species}')

    def stats(self):
        """display the stats of the pokemon"""
        print(f"---{self.species}---------")
        print(f"     Name: {self.name}")
        print(f"     Type: {self.type}")
        print(f"     Shiny: {self.shiny}")
        print(f"     Level: {self.level}")
        print(f"     age: {self.age}")


class Charmander(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "Charmander"
        self.species = "Charmander"
        self.type = "Fire"

    def ember(self):
        print(f"{self.name} used ember")


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "Squirtle"
        self.species = "Squirtle"
        self.type = "water"
        self.has_sun_glasses = True

    def water_gun(self):
        """use the water gun attack"""
        print(f"{self.name} used water gun.")


if __name__ == "__main__":
    pokemon_one = Pokemon()
    print("Pokemon Name:", pokemon_one.name)
    pokemon_one.name = "Gary"
    print("Pokemon Name:", pokemon_one.name)

    pokemon_two = Pokemon()
    print("Pokemon twos Name:", pokemon_two.name)

    if pokemon_one == pokemon_two:
        print("These are the same pokemon")

    else:
        print("No they're different")

        if type(pokemon_one) is Pokemon:
            print(f"{pokemon_one.name} is a Pokemon")

            if type(pokemon_two) is Pokemon:
                print(f"{pokemon_two.name} is a Pokemon")

    pokemon_one.stats()
    pokemon_two.stats()

    squirtle_one = Squirtle()
    squirtle_one.talk()
    squirtle_one.water_gun()

charmander_one = Charmander()
charmander_one.talk()
charmander_one.ember()
