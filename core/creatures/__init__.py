from core.creatures.creature import Creature


class Rabbit(Creature):
    def __init__(self, name='Rabbit', hp=5, damage=2, lvl=1):
        super().__init__(name, hp, damage, lvl)


class Wolf(Creature):
    def __init__(self, name='Wolf', hp=10, damage=5, lvl=1):
        super().__init__(name, hp, damage, lvl)


class Bear(Creature):
    def __init__(self, name='Bear', hp=25, damage=10, lvl=1):
        super().__init__(name, hp, damage, lvl)
