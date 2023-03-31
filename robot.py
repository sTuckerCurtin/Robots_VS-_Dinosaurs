from weapon import Weapon



class Robot:
    def __init__(self, name,):
        self.name = ""
        self.health = 100
        self.active_weapon = Weapon()


    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attackpower 
        print(f"{self.name} has attacked {dinosaur} for {self.active_weapon.attack_power} damage!")
        