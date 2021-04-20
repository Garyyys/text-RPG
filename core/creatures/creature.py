class Creature:
    """
    Base Creature class.
        - name:   creature name
        - hp:     creature health points
        - damage: creature damage
        - lvl:    creature level
    """

    def __init__(self, name='Creature', hp=5, damage=1, lvl=1):
        """
        Creature constructor
        :param name:   creature name
        :param hp:     creture health points
        :param damage: creture damage
        :param lvl:    creature level
        """
        self.name = name
        self.hp = hp * lvl
        self.damage = damage * lvl
        self.lvl = lvl

    def is_dead(self):
        """
        Returns true if no health points left for creature.
        :returns bool:
        """
        return self.hp <= 0

    def attack(self, enemy):
        """
        Performs attack on given enemy
        :param enemy: Enemy creature
        :returns bool: Returns True if it was victorious strike
        """
        if self.is_dead() or enemy.is_dead():
            return False

        enemy.hp -= self.damage

        print(f"{self.name} deals {self.damage} damage to {enemy.name}")

        return enemy.is_dead()

    def __repr__(self):
        """
        Object text representation
        :returns str:
        """
        return f"<{self.__class__.__name__}: {self.name} {self.lvl} lvl; hp: {self.hp} dmg: {self.damage}>"
