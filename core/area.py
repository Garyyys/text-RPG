from random import random
from core.creatures import Rabbit, Wolf, Bear


class Area:
    def __init__(self, name, parent=None):
        """
        Area constructor
        :param name: Area name
        :param parent:
        """
        self.name = name
        self.parent = parent

        if parent:
            parent.add_child(self)

        self.children = []

    def add_child(self, child):
        """
        Appends new area to children list.
        """
        if child not in self.children:
            self.children.append(child)

    def get_directions(self):
        """
        Rtruns list of adventure directions
        """

        directions = self.children[:]

        if self.parent:
            directions.append(self.parent)

        return directions

    def render(self, player):
        """
        Displays area information
        """
        print(f"Area: {self}")
        print(player)

    def get_choice(self):
        """
        Prompts user choice via input() function.
        :returns int|str:
        """
        choice = input()

        if choice.isdigit():
            choice = int(choice)

        return choice

    def walk(self, player):
        self.render(player)

        directions = self.get_directions()
        directions_range = range(len(directions))

        for i in directions_range:
            print(f"{i}. {directions[i].name}")

        choice = self.get_choice()

        if choice not in directions_range:
            print("Incorrect way")
            return self.walk(player)

        directions[choice].walk(player)

    def __repr__(self):
        """
        Area text representation
        :returns str:
        """
        return f"<{self.__class__.__name__}: {self.name}>"


class City(Area):
    pass


class Forest(Area):
    CHOICE_ATTACK = 0
    CHOICE_RUN_AWAY = 1

    def render(self, player, enemy=None):
        super().render(player)

        if enemy:
            print(enemy)

    def fight(self, player, enemy):
        self.render(player, enemy)

        combat_options = ['Attack', 'Run Away']
        combat_options_range = range(len(combat_options))

        for i in combat_options_range:
            print(f"{i}. {combat_options[i]}")

        choice = self.get_choice()

        if choice not in combat_options_range:
            print("Invalid choice")
            return self.fight(player, enemy)

        if choice == self.CHOICE_ATTACK:
            if player.attack(enemy):
                print(f"{enemy.name} has beed slain")
                return self.walk(player)

        if enemy.attack(player):
            print(f"{player.name} has beed slain")
            print("Game over")
            quit(1)

        return self.fight(player, enemy)

    def walk(self, player):
        enemies = [Rabbit, Wolf, Bear]
        enemies_range = range(len(enemies))

        dice = round(random() * 10)

        if dice in enemies_range:
            enemy = enemies[dice]()
            self.fight(player, enemy)

        return super().walk(player)
