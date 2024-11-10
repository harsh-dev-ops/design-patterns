class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self) -> None:
        self.stats = [1, 1, 1]

    @property
    def strength(self):
        return self.stats[self._strength]

    @property
    def agility(self):
        return self.stats[self._agility]

    @property
    def intelligence(self):
        return self.stats[self._intelligence]

    @strength.setter
    def strength(self, value):
        self.stats[self._strength] = value

    @agility.setter
    def agility(self, value):
        self.stats[self._agility] = value

    @intelligence.setter
    def intelligence(self, value):
        self.stats[self._intelligence] = value

    @property
    def avg_stats(self):
        return float(sum(self.stats) / len(self.stats))

    @property
    def num_stats(self):
        return len(self.stats)

    def __str__(self):
        return f"(Strength:{self.strength} / Attack:{self.agility} / Intelligence:{self.intelligence})"


if __name__ == '__main__':
    creature = Creature()

    print(creature)
