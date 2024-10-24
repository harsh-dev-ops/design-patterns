class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as a {self.position}'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self, person=None):
        if person is None:
            self.person = Person()
        else:
            self.person = person

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):

    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):

    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):

    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == "__main__":
    p = PersonBirthDateBuilder()

    me = p.called("Harsh").\
        works_as_a("Dev Ops").\
        born("01-02-2000").\
        build()
    print(me)
