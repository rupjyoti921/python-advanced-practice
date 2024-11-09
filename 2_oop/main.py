from enemy import *

ene1=Enemy()
ene1.type_of_enemy="Zombie"
print(f"{ene1.type_of_enemy} has {ene1.health_point} health points and can do attack of {ene1.attack_damage}")

ene1.talk()
ene1.walk_forward()
ene1.attack()
print()

ene2=Enemy()
ene2.type_of_enemy="Danab"
ene2.attack_damage=5
ene2.health_point=20
ene2.talk()
ene2.walk_forward()
ene2.attack()