from abc import ABC, abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name
        

# ------------------ Without DIP ----------------------------- #

class Relationships:
    relations = []
    
    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

class Research:
    def __init__(self, relationships: Relationships):
        relations = relationships.relations
        for r in relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f"{r[2].name} is the child of {r[0].name}")

# ------------------------- DIP ------------------------------ #

class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, person: Person):
        pass

class Relationships(RelationshipBrowser):
    relations = []
    
    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))
        
    def find_all_children_of(self, person: Person):
        for relation in self.relations:
            if relation[0].name == person.name and relation[1] == Relationship.PARENT:
                yield relation[2].name
        

class Research:
    def __init__(self, browser: RelationshipBrowser, person):
        for child_name in browser.find_all_children_of(person):
            print(f'{person.name} has a child called {child_name}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# low-level module
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships, parent)
    