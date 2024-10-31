import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        f = open("Creational/Singleton/population.txt", "r")
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] = int(lines[i+1].strip())

        f.close()


class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for city in cities:
            result += Database().population[city]

        return result


class ConfigurableRecordFinder:
    def __init__(self, db: Database):
        self.db = db

    def total_population(self, cities):
        result = 0
        for city in cities:
            result += self.db.population[city]

        return result


class DummyDatabase:
    population = {
        'a': 1,
        'b': 2,
        'c': 3
    }

    def get_population(self, name):
        return self.population[name]


class SingletonTest(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_total_population(self):
        rf = SingletonRecordFinder()

        cities = ['Tokyo', 'Mexico']

        tp = rf.total_population(cities)

        self.assertEqual(3300000 + 2500000, tp)

    def test_dependent_total_population(self):
        ddb = DummyDatabase()
        crf = ConfigurableRecordFinder(ddb)
        self.assertEqual(
            crf.total_population(['a', 'b']),
            3
        )


if __name__ == '__main__':
    unittest.main()
