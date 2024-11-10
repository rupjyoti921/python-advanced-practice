class Enemy:

    def __init__(self, type_of_enemy, health_points=10,attack_damage=1):    #No Argument Constructor
         self.__type_of_enemy=type_of_enemy
         self.health_point=health_points
         self.attack_damage=attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")
    
    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")


class Zombie(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Zombie", health_points=health_points,attack_damage=attack_damage)

    def talk(self):
        print("*Grumbling...*")
    
    def spread_disease(self):
        print("The Zombie is trying to spread the infection")


class Ogre(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Ogre", health_points=health_points,attack_damage=attack_damage)

    def talk(self):
        print("Ogre is slamming hands all around.")
    