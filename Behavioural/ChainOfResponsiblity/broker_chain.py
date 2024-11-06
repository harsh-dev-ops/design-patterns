# Event
# Query
# Command


from abc import ABC
import enum
from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


class CreatureAttributes(enum.Enum):
    ATTACK = 1
    DEFENSE = 2
    HP = 3
    MP = 4


class Query:
    def __init__(self, creature_name, creature_attribute, default_value):
        self.creature_name = creature_name
        self.value = default_value
        self.creature_attribute = creature_attribute


class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query: Query):
        self.queries(sender, query)


class Creature:
    def __init__(self,
                 game: Game,
                 name: str,
                 attack: int = 1,
                 defense: int = 1,
                 hp: int = 100,
                 mp: int = 100
                 ):

        self.game = game
        self.name = name
        self._attack = attack
        self._defense = defense
        self._hp = hp
        self._mp = mp

    @property
    def attack(self):
        q = Query(self.name, CreatureAttributes.ATTACK, self._attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, CreatureAttributes.DEFENSE, self._defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier(ABC):
    def __init__(self, game: Game, creature: Creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    def handle(self, sender: Creature, query: Query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query):
        if (sender.name == query.creature_name) and (query.creature_attribute == CreatureAttributes.ATTACK):
            query.value *= 2


class DoubleDefenseModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query):
        if sender.name == query.creature_name and query.creature_attribute == CreatureAttributes.ATTACK:
            query.value *= 2


if __name__ == '__main__':
    game = Game()
    goblin = Creature(game, 'Strong Goblin', 2, 2)

    print(goblin)

    with DoubleAttackModifier(game, goblin):
        print(goblin)

    print(goblin)
