from unittest import TestCase


class Person:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class PersonFactory:
    id = 1

    def create_person(self, name):
        p = Person(self.id, name)
        self.id += 1
        return p


class Evaluate(TestCase):
    def test_exercise(self):
        pf = PersonFactory()

        p1 = pf.create_person('Chris')
        self.assertEqual(p1.name, 'Chris', "PASSED")
        self.assertEqual(p1.id, 1, "PASSED")

        p2 = pf.create_person('Jane')
        self.assertEqual(p2.name, 'Jane', "PASSED")
        self.assertEqual(p2.id, 2, "PASSED")


evaluate = Evaluate()

try:
    evaluate.test_exercise()
    print("PASSED")
except AssertionError as ae:
    print(f"{ae}")
    print("FAILED")
