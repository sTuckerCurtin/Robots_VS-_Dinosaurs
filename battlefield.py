from dinosaur import Dinosaur
from robot import Robot



class Battlefield:
    def __init__(self):
        self.robot = ""
        self.dinosaur = ""


    def run_game(self):
        run = input("Do you want to play Robot Vs Dinosaur: Fall of Humanity")
        
    


    def display_welcome(self):
        print("Welcome to the Thunder Dome! Two Champions enter...One leaves! Ready. Set. Fight!")


    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            if self.robot.health <= 0:
                print(f"{self.dinosaur.name} is the Winner! ")
                break
            self.dinosaur.attack(self.robot)
            if self.dinosaur.health <= 0:
                print(f"{self.dinosaur} is the Winner!")
            



    def display_winner(self):
        pass
        

