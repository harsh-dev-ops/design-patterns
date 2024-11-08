from abc import ABC, abstractmethod
from enum import Enum
import unittest


class BankAccount:

    def __init__(self, balance: int | float = 0, overdraft_limit: int | float = -10):
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
    def __init__(self):
        self.success = True

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
        super().__init__()
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


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=[]):
        super().__init__()
        for cmd in items:
            self.append(cmd)

    def invoke(self):
        for cmd in self:
            cmd.invoke()

    def undo(self):
        for cmd in self:
            cmd.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, ba1: BankAccount, ba2: BankAccount, amount: int | float):
        super().__init__([
            BankAccountCommand(
                ba1, BankAccountCommand.Action.WITHDRAW, amount),
            BankAccountCommand(
                ba2, BankAccountCommand.Action.DEPOSIT, amount)
        ])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False

        self.success = ok


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        ba = BankAccount()
        deposit1 = BankAccountCommand(
            ba, BankAccountCommand.Action.DEPOSIT, 100)
        deposit2 = BankAccountCommand(
            ba, BankAccountCommand.Action.DEPOSIT, 200)

        composite_cmd = CompositeBankAccountCommand([deposit1, deposit2])

        print(ba)
        composite_cmd.invoke()
        print(ba)

        self.assertEqual(ba.balance, 300)

        composite_cmd.undo()
        print(ba)
        self.assertEqual(ba.balance, 0)

    def test_transfer_fail(self):
        print()
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 100
        wc = BankAccountCommand(
            ba1, BankAccountCommand.Action.WITHDRAW, amount)
        dc = BankAccountCommand(
            ba2, BankAccountCommand.Action.DEPOSIT, amount)

        transfer = CompositeBankAccountCommand([wc, dc])

        print('ba1:', ba1, 'ba2:', ba2)
        transfer.invoke()

        print('ba1:', ba1, 'ba2:', ba2)
        transfer.undo()
        print('ba1:', ba1, 'ba2:', ba2)

    def test_better_transfer(self):
        print("Better Transfer Test")
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        transfer = MoneyTransferCommand(ba1, ba2, 100)

        print('ba1:', ba1, 'ba2:', ba2)
        transfer.invoke()

        print('ba1:', ba1, 'ba2:', ba2)
        transfer.undo()
        print('ba1:', ba1, 'ba2:', ba2)
        print(transfer.success)


if __name__ == "__main__":
    unittest.main()
