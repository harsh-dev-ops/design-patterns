from abc import ABC, abstractmethod
from enum import Enum, auto


class HotDrink(ABC):

    @abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is nice but I\'d prefer it with milk")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious.")


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories: list[tuple[str, HotDrinkFactory]] = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))
                self.initialized = True

    def make_drink(self) -> HotDrink:
        print("Available Drink")
        for f in self.factories:
            print(f[0])

        s = input(f"Please pick drink (0-{len(self.factories)-1})")
        idx = int(s)
        s = input(f"Specify Milk Amount: ")
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == "__main__":
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
