from abc import ABC, abstractmethod
from collections.abc import Iterable
import unittest


class Box(Iterable, ABC):

    @property
    def amount(self):
        result = 0

        for s in self:
            for c in s:
                if isinstance(c, list or tuple):
                    for j in c:
                        result += j.price
                else:
                    result += c.price
        return result


class Product(Box):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __iter__(self):
        yield self


class GiftBox(list, Box):
    def __init__(self, name: str = "Gift Box"):
        super().__init__()
        self.name = name


class Cart(list, Box):
    pass


class TestCart(unittest.TestCase):
    def test_cart_price(self):
        phone = Product('iPhone 16', 999)
        tablet = Product('iPad Pro 12.9 inch', 1299)
        charger = Product('iPhone Charger', 100)

        giftbox = GiftBox('Happy Birthday')
        giftbox.append(tablet)
        giftbox.append(charger)

        cart = Cart()
        cart.append(phone)
        cart.append(giftbox)

        self.assertEqual(cart.amount, 2398)


if __name__ == "__main__":
    unittest.main()
