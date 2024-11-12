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

    @property
    def can_vote(self):
        return self.age >= 18

    @age.setter
    def age(self, value):
        if self._age == value:
            return

        old_can_vote = self.can_vote

        self._age = value
        self.property_changed('age', value)

        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)


class TrafficAuthority:
    def __init__(self, person: Person):
        self.person = person
        self.person.property_changed.append(
            self.person_changed
        )

    def person_changed(self, name, value):
        if name == 'age':
            if value < 18:
                # print("You can't drive")
                return
            else:
                print("You can drive")
                self.person.property_changed.remove(
                    self.person_changed)


class ElectionComission:
    def __init__(self, person: Person):
        self.person = person
        self.person.property_changed.append(
            self.person_changed
        )

    def person_changed(self, name, value):
        if name == 'can_vote':
            print(f"Voting status changed to {value}")
            self.person.property_changed.remove(
                self.person_changed)


if __name__ == '__main__':

    person = Person()
    ta = TrafficAuthority(person)
    ec = ElectionComission(person)

    for age in range(14, 25):
        print(f"Setting age to {age}")
        person.age = age
