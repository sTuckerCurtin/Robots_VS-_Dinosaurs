class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power



    
        

    def weapon_select(self):
        weapon1 = Weapon("The Toilet Brush of Death", 15)
        weapon2 = Weapon("A Dumptruck Full of Microwaves", 20)
        weapon3 = Weapon("The Rock of Freedom", 15)

        weapon_selector = input(f"Please Choose your weapon. Press 1 for {weapon1.name}. Press 2 for {weapon2.name}. Press 3 for {weapon3}")
        if weapon_selector == "1":
            print(f"You have choosen {weapon1}")
            self.active_weapon = weapon1
        elif weapon_selector == "2":
            print(f"You have choosen {weapon2}")
            self.active_weapon == weapon2
        else:
            print(f"You have selected {weapon3}")
            self.active_weapon == weapon3
        