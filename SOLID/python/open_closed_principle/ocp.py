from abc import ABC, abstractmethod
from enum import Enum
import types
from typing import Any

class Color(Enum):
    RED = 1
    GREEN = 2
    ORANGE = 3
    BLUE = 4
   
    
class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
  
    
class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
        

class ProductFilter:
    def filter_by_color(self, products:list, color):
        for p in products:
            if p.color == color:
                yield p
    
    def filter_by_size(self, products:list, size):
        for p in products:
            if p.size == size:
                yield p
   
    def filter_by_size_and_color(self, products:list, size, color):
       for p in products:
           if p.size==size and p.color==color:
               yield p

    # state space explosion
    # 3 criteria
    # s c w cs sw cw csw = 7 methods
    
    # Open Close Principle (OCP) = Open for extension and closed for modifications
    
# New methodology
class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        pass
    
    def __or__(self, other):
        pass
    
class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec2 = spec2
        self.spec1 = spec1

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)
            

class OrSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2
        
    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) or self.spec2.is_satisfied(item)
    

class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color
    
    def __and__(self, other):
        return AndSpecification(self, other)
    
    def __or__(self, other):
        return OrSpecification(self, other)


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size
    
    def __and__(self, other):
        return AndSpecification(self, other)
    
    def __or__(self, other):
        return OrSpecification(self, other)
    
    
class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item
    

apple = Product('Apple', Color.GREEN, Size.SMALL)     
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)
table = Product('Table', Color.BLUE, Size.MEDIUM)

products = [apple, tree, house]     

#------------------------ Old Filter -------------------------------#
print('Old Method:\n')     
pf = ProductFilter()
for p in pf.filter_by_color(products, Color.GREEN):
    print(p.name, p.color.name, p.size.name)
    


#------------------------ New Filter -------------------------------#
bf = BetterFilter()

print("-"*50)
print('\nNew Method:\n')
print('Green Color Objects:')
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(p.name, p.color.name)

print('\nSize: Large')
largeSize = SizeSpecification(Size.LARGE)
for p in bf.filter(products, largeSize):
    print(p.name,  p.size.name)
    
print('\nSize: Large and Color: Blue')
blueColor_largeSize = ColorSpecification(Color.BLUE) and SizeSpecification(Size.LARGE)
for p in bf.filter(products, blueColor_largeSize):
    print(p.name, p.size.name, p.color.name)
    
print('\nSize: Large or Color: Green')
color_size = ColorSpecification(Color.GREEN) or SizeSpecification(Size.LARGE)
for p in bf.filter(products, color_size):
    print(p.name, p.color.name, p.size.name)