import time
from actors import Wizard, Creature, SmallAnimal, Dragon
import random


def main():
    print_header()
    game_loop()


def print_header():
    print("--------------------------")
    print("     WIZARD GAME APP      ")
    print("--------------------------")
    print("--------------------------")
    print()


def game_loop():

    creatures = [
        SmallAnimal("Toad", 1),
        Creature("Tiger", 12),
        SmallAnimal("Bat", 3),
        Dragon("Dragon", 50, 75, True),
        Wizard("Evil Wizard", 1000)
    ]

    hero = Wizard("Gandolf", 75)

    while True:
        active_creature = random.choice(creatures)
        print("{} has appeared from dark and foggy forest"
              .format(active_creature))

        cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around? ")
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized")
        elif cmd == 'r':
            print("The wizard has become unsure of his power and flies!!!!")
        elif cmd == 'l':
            print("The wizard takes in the surroundings and sees:")
            for c in creatures:
                print(" * A {} of level {}".format(c.name, c.level))
        else:
            print("Ok exiting game... bye")
            break

        if not creatures:
            print("You`ve defeated all the creatures, well done")


if __name__ == '__main__':
    main()
