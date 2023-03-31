from weapon import Weapon
from dinosaur import Dinosaur


class Robot:
    def __init__(self, name,):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Rock of Freedom", 15)


    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power 
        print(f"{self.name} has attacked {dinosaur.name} with the {self.active_weapon.name } for {self.active_weapon.attack_power} damage!")
        