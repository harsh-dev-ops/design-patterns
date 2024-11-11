class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance: int | float = 10):
        self.balance = balance
        self.states = [Memento(self.balance)]
        self.current_state_idx = 0

    def deposit(self, amount: int | float):
        self.balance += amount
        m = Memento(self.balance)
        self.states.append(m)
        self.current_state_idx += 1
        return m

    def restore(self, memento: Memento):
        if memento:
            self.balance = memento.balance
            self.states.append(memento)
            self.current_state_idx = len(self.states) - 1

    def undo(self):
        if self.current_state_idx > 0:
            self.current_state_idx -= 1
            m = self.states[self.current_state_idx]
            self.balance = m.balance
            return m
        return None

    def redo(self):
        if self.current_state_idx + 1 < len(self.states):
            self.current_state_idx += 1
            m = self.states[self.current_state_idx]
            self.balance = m.balance
            return m
        return None

    def __str__(self):
        return f"Balance: {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(100)
    print(ba)

    m1 = ba.deposit(20)
    m2 = ba.deposit(30)

    print(ba)

    ba.undo()
    print(f'Undo 1: {ba}')
    ba.undo()
    print(f'Undo 2: {ba}')
    ba.redo()
    print(f'Redo 1: {ba}')
