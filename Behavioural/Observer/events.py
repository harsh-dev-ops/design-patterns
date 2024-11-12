from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(person_name, person_address):
    print(f"A doctor has been called to {person_address} for {person_name}")


if __name__ == '__main__':
    person = Person('John', '122 London Street')
    person.falls_ill.append(call_doctor)
    person.catch_a_cold()
