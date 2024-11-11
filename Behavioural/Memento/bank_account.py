class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance: int | float = 10):
        self.balance = balance

    def deposit(self, amount: int | float):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento: Memento):
        self.balance = memento.balance

    def __str__(self):
        return f"Balance: {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(100)
    print(ba)

    m1 = ba.deposit(20)
    m2 = ba.deposit(30)

    print(ba)

    ba.restore(m1)
    print(ba)
    ba.restore(m2)

    print(ba)
