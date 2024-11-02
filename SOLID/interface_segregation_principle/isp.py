from abc import ABC, abstractmethod


# ---------------------- Without ISP ---------------------- #
class Machine(ABC):
    
    @abstractmethod
    def fax(self, document):
        pass
    
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionPrinter(Machine):
    
    def print(self, document):
        pass
    
    def scan(self, document):
        pass
    
    def fax(self, document):
        raise NotImplemented()
    
    

class MultiFunctionFax(Machine):
    
    def fax(self, document):
        pass
    
    def print(self, document):
        pass
    
    def scan(self, document):
        raise NotImplemented()
    

# --------------------- With ISP ------------------------- #

class Scanner(ABC):
    
    @abstractmethod
    def scan(self, document):
        pass
    

class Printer(ABC):
    
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    
    @abstractmethod
    def fax(self):
        pass
    

class MultiFunctionPrinter(Printer, Scanner):
    def print(self, document):
        pass
    
    def scan(self, document):
        pass
    

class MultiFunctionFax(Fax, Printer):
    def fax(self, document):
        pass
    
    def print(self, document):
        pass
    
