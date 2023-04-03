from weapon import Weapon
from dinosaur import Dinosaur


class Robot:
    def __init__(self, name,):
        self.name = name
        self.health = 100
        self.active_weapon = None
        
              


    def attack(self, dinosaur):
        if self.active_weapon is not None:
            dinosaur.health -= self.active_weapon.attack_power 
        print(f"{self.name} has attacked {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage!")
        


        
 
    def weapon_select(self):
        weapon1 = Weapon("The Toilet Brush of Death", 15)
        weapon2 = Weapon("A Dumptruck Full of Microwaves", 25)
        weapon3 = Weapon("The Rock of Freedom", 15)

        weapon_selector = input(f"Please Choose your weapon. Press 1 for {weapon1.name}. Press 2 for {weapon2.name}. Press 3 for {weapon3.name} ")
        if weapon_selector == "1":
            print(f"You have choosen {weapon1.name}")
            self.active_weapon = weapon1
        elif weapon_selector == "2":
            print(f"You have choosen {weapon2.name}")
            self.active_weapon = weapon2
        else:
            print(f"You have selected {weapon3.name}")
            self.active_weapon = weapon3
       
       