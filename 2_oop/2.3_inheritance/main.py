from enemy import *

ene1=Enemy("Zombie")
# print(f"{ene1.type_of_enemy} has {ene1.health_point} health points and can do attack of {ene1.attack_damage}")

ene1.talk()
ene1.walk_forward()
ene1.attack()
print("enemy1 is type of ", ene1.get_type_of_enemy())
print()

ene2=Enemy("Danab",20,2)
# print(f"{ene2.type_of_enemy} has {ene2.health_point} health points and can do attack of {ene2.attack_damage}")

ene2.talk()
ene2.walk_forward()
ene2.attack()
print("enemy2 is type of "+ ene2.get_type_of_enemy())
print("--------------------------------------------------------------")
print("")

zombie1=Zombie(10,2)
zombie1.talk()

oger1=Ogre(20,4)
oger1.talk()


print()
