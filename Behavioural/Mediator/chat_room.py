from typing import List, Set


class Person:
    def __init__(self, name) -> None:
        self.name: str = name
        self.room: ChatRoom = None
        self.chat_log = []

    def receive(self, sender, message):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

    def private_message(self, who: str, message: str):
        self.room.message(self.name, who, message)

    def say(self, message):
        self.room.broadcast(self.name, message)

    def __str__(self):
        return f"{self.name}"


class ChatRoom:
    def __init__(self):
        self.people: Set[Person] = set()

    def broadcast(self, source: str, message: str):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def join(self, person: Person):
        if person in self.people:
            return
        join_msg = f"{person.name} joins the room."
        self.broadcast("room", join_msg)
        person.room = self
        self.people.add(person)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


if __name__ == '__main__':
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")

    room.join(john)
    room.join(jane)

    john.say('hi')

    jane.say('oh, hey john')

    simon = Person('Simon')
    room.join(simon)
    simon.say('hi everyone!')

    jane.private_message("Simon", "Hey Simon, Glad you could join us.")
