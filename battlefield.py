from dinosaur import Dinosaur
from robot import Robot




class Battlefield:
    def __init__(self):
        self.robot = Robot("RoBob")
        self.dinosaur = Dinosaur("Super Mega Dino", 25)


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
            
        
    


    def display_welcome(self):
        print()
        print("In year 2077. Dr. Sam Curtin discovered a fully preserved Dinosaur under a sheet of ice in the Arctic Circle, thats been melted away by climate change. While the Dinosaur was being studied it woke up and started charging toward Northern Canada ! With the Dinosaur terrorizing the Canucks, mankind built the ultimate weapon to fight this beast...his name was .....RoBob  ")
        print()


    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            if self.robot.health <= 0:
                print(f"{self.dinosaur.name} is the Winner! ")
                break
            self.dinosaur.attack(self.robot)
            if self.dinosaur.health <= 0:
                print(f"{self.dinosaur.name} is the Winner!")
            



    def display_winner(self):
        if self.dinosaur.health > self.robot.health:
            print()
            print(f"All Hail {self.dinosaur.name}, The new King of The World....Humanity will become extinct and the era of the Dinosaur will start again ")
        elif self.robot.health > self.dinosaur.health:
            print()
            print(f"{self.robot.name} has won! Humanity is saved!")
        else:
            print("It's a tie!")

       
       
       
       
       
       
        

