from enemy import *

def battle(e: Enemy):
    e.talk()
    e.attack()

zombie1=Zombie(10,2)
oger1=Ogre(20,4)

battle(zombie1)
battle(oger1)

print()
