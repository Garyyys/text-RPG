from core.area import Area, City, Forest
from core.creatures import Creature


def main():
    world = Area('Azeroth')
    city = City('Ironforge', world)
    forest = Forest('Sherwood', world)

    # TODO: load saved game or start new game

    player = Creature('Tirion Foldring', lvl=20)

    world.walk(player)



if __name__ == '__main__':
    main()
