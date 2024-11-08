from abc import ABC, abstractmethod
from enum import Enum


class BankAccount:

    def __init__(self, balance: int | float = 0, overdraft_limit: int | float = -100):
        self.balance = balance
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount: int | float):
        if self.balance - amount >= self._overdraft_limit:
            self.balance -= amount
            print(f"Withdraw: {amount}, Balance: {self.balance}")
            return True
        return False

    def deposit(self, amount: int | float):
        self.balance += amount
        print(f"Deposit: {amount}, Balance: {self.balance}")
        return True

    def __str__(self):
        return f"Balance: {self.balance}"


class Command(ABC):
    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account: BankAccount, action, amount: int | float) -> None:
        self.account = account
        self.action:  BankAccountCommand.Action = action
        self.amount = amount
        self.success = None

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return

        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == "__main__":
    ba = BankAccount(1000, -100)

    cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)

    print(ba)
    cmd.invoke()

    print(ba)

    cmd.undo()
    print(ba)

    cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 10000)

    print(ba)

    cmd.invoke()

    print(ba)

    cmd.undo()
    print(ba)
