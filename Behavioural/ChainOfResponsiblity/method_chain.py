class Creature:
    def __init__(
        self,
        name: str,
        attack: int | float,
        defense: int | float
    ) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier:
    def __init__(self, creature: Creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling Attack of the {self.creature.name}")
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Doubling Defense of the {self.creature.name}")
            self.creature.defense += 1
        else:
            print(f"Creature attack is greater than threshold")
        super().handle()


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print("All Bonus has been disabled for creature")


if __name__ == '__main__':
    goblin = Creature("Goblin", 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)

    root.add_modifier(NoBonusesModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))

    root.handle()

    print(goblin)
