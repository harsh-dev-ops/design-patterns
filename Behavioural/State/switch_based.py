import enum


class Lock:
    class State(enum.Enum):
        LOCKED = enum.auto()
        FAILED = enum.auto()
        UNLOCKED = enum.auto()

    def __init__(self, code: str):
        self.code = code
        self.state = Lock.State.LOCKED

    def check_code(self, code: str):
        if self.code == code:
            self.state = Lock.State.UNLOCKED
        self.state = Lock.State.FAILED


if __name__ == '__main__':
    lock = Lock('1234')

    entry = ''
    while (lock.state == Lock.State.LOCKED):
        entry += input(entry)
        if len(entry) == len(lock.code):
            break

    lock.check_code(entry)
    print(lock.state)
