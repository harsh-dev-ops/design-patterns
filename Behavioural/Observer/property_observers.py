from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age=0) -> None:
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        self.property_changed('age', value)


class TrafficAuthority:
    def __init__(self, person: Person):
        self.person = person
        self.person.property_changed.append(
            self.person_changed
        )

    def person_changed(self, name, value):
        if name == 'age':
            if value < 18:
                print("You can't drive")
            else:
                print("You can drive")
                self.person.property_changed.remove(
                    self.person_changed)


if __name__ == '__main__':
    person = Person()
    ta = TrafficAuthority(person)
    for age in range(14, 25):
        print(f"Setting age to {age}")
        person.age = age
