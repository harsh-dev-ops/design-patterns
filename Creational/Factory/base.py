from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class Creator1(Creator):
    def factory_method(self) -> Product:
        return Product1()


class Creator2(Creator):
    def factory_method(self):
        return Product2()


class Product1(Product):
    def operation(self):
        return "{Result of the Product1}"


class Product2(Product):
    def operation(self):
        return "{Result of the Product2}"


def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the Creator1.")
    client_code(Creator1())
    print("\n")

    print("App: Launched with the Creator2.")
    client_code(Creator2())
