from typing import Any


class Singleton(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwds)

        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self, session: Any = 'dev_session'):
        self.session = session
        print("Loading database")

    def get_session(self):
        yield self.session

    def __str__(self):
        return str(self.session)


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)

    d2.session = 'test_session'

    print(d1.session, d2.session, Database().session,
          next(Database().get_session()))
    print(d1.session == d2.session == Database().session ==
          next(Database().get_session()))

    get_d1_session = next(d1.get_session())
    get_d2_session = next(d2.get_session())

    print(get_d1_session, get_d2_session)
