class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
        
    def remove_entry(self, pos):
        del self.entries[pos]
    
    def __str__(self):
        return '\n'.join(self.entries)
    
    # Break Single Responsibility Principle
    def save(self, filepath):
        file = open(filepath, "w")
        file.write(f'{self}')
        file.close
    
    def load(self, filepath):
        pass
    
    def load_from_web(self, uri):
        pass
    

class PersistenceManager:
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(f'{journal}')
        file.close()
    
    def read_from_file(filename):
        file = open(filename, "r")
        print(file.read())
        file.close()
        

j = Journal()
j.add_entry("I want to eat a cheesecake.")
j.add_entry("I want to drink coffee after that.")
j.add_entry("I want to go for a walk.")
# j.save('1. SOLID/1. SRP: Single Responsibility Principle.py/file.txt')

PersistenceManager.save_to_file(j, '1. SOLID/1. SRP: Single Responsibility Principle.py/file.txt')
PersistenceManager.read_from_file('1. SOLID/1. SRP: Single Responsibility Principle.py/file.txt')

