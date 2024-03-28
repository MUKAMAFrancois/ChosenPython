#intro to classes

# Introduction to Classes and Objects

# What are classes and objects?
# - Classes are blueprints or templates for creating objects in Python.
# - Objects are instances of classes that encapsulate data (attributes) and behavior (methods).

# Example 1: Defining a simple class
class Car:
    pass

# Creating objects of the Car class
car1 = Car()
car2 = Car()

# Understanding the concept of encapsulation, abstraction, inheritance, and polymorphism.

# Encapsulation: Bundling data (attributes) and methods (behavior) within a class to hide implementation details from the outside world.
# Abstraction: Simplifying complex systems by hiding unnecessary details and exposing only relevant features to the user.
# Inheritance: Deriving new classes (subclasses) from existing classes (superclasses) to reuse and extend functionality.
# Polymorphism: Ability of objects to take on multiple forms or behaviors based on their context or type.

# Example 2: Implementing encapsulation and abstraction
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Encapsulating name attribute
        self.salary = salary  # Encapsulating salary attribute
    
    def display_details(self):  # Abstraction of method to display employee details
        print(f"Name: {self.name}, Salary: ${self.salary}")

# Example 3: Implementing inheritance and polymorphism
class Animal:
    def speak(self):
        pass  # Abstract method
    
class Dog(Animal):  # Inheriting from the Animal class
    def speak(self):  # Polymorphic method overriding
        return "Woof!"

class Cat(Animal):  # Inheriting from the Animal class
    def speak(self):  # Polymorphic method overriding
        return "Meow!"

# Basic syntax for defining classes and creating objects

# Example 4: Defining a class with attributes and methods
class Rectangle:
    def __init__(self, width, height):  # Constructor method
        self.width = width  # Instance attribute
        self.height = height  # Instance attribute
    
    def area(self):  # Instance method
        return self.width * self.height

# Creating objects of the Rectangle class
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(3, 7)




#example 5:


class Hotel:
    def __init__(self,name,number_of_rooms,location,cost):
        self.name = name
        self.number_of_rooms = number_of_rooms
        self.location = location
        self.cost = cost

    def hotel_intro(self):
        print(f"Welcome to {self.name} located in {self.location} with {self.number_of_rooms} rooms.")

    def price_to_pay(self,days,households):
        return days * households * self.cost
    

hotel1=Hotel("Mariot",102,"Kigali",100)
hotel1.hotel_intro()
print(f"Price to pay for 5 days and 2 households is ${hotel1.price_to_pay(5,2)}")






#instance attributes Vs class attributes
class Circle:
    pi= 22/7
    
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return Circle.pi* self.radius**2
        

c1=Circle(20)
area=c1.area()
print(round(area,2)) # 1257.14




# Class Methods and Static Methods

# In Python, class methods are methods that are bound to a class
# rather than an instance of the class. They are defined using the @classmethod 
# decorator and can be accessed 
# and called on the class itself, without the need for creating an instance of the class


#ex1:
class MyClass:
    class_attribute = 10
    
    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute
    
    @classmethod
    def class_method(cls):
        print("This is a class method.")
        print("Class attribute:", cls.class_attribute)
    
    def instance_method(self):
        print("This is an instance method.")
        print("Instance attribute:", self.instance_attribute)


# Calling a class method on the class itself
MyClass.class_method()
# Output:
# This is a class method.
# Class attribute: 10

# Creating an instance of the class
obj = MyClass(20)
# Calling an instance method on the instance
obj.instance_method()
# Output:
# This is an instance method.
# Instance attribute: 20


#ex2:


class Hotel:
    workers=105

    def __init__(self,name,number_of_rooms,location,cost):
        self.name = name
        self.number_of_rooms = number_of_rooms
        self.location = location
        self.cost = cost

    @classmethod
    def hotel_intro(cls):
        print(f"Welcome to our hotel with {cls.workers} workers.")

    @classmethod
    def total_payment(cls,salary_per_worker):
        return cls.workers * salary_per_worker
    

hotel2=Hotel("Serena",200,"Kigali",150)
Hotel.hotel_intro()  # Welcome to our hotel with 105 workers.

print(f"Total payment for workers is ${hotel2.total_payment(900)}")  #Total payment for workers is $94500



# Here are the key characteristics of static methods:

# They are defined using the @staticmethod decorator, followed by a method definition.
# Static methods do not receive any special first parameter like self or cls. 
# They behave like regular functions and do not have access to the instance or class.

# They are independent of the state of the instance or the class and cannot access or modify instance or class attributes.
# Static methods are usually used when a method does not require access to instance-specific or class-specific data and can be implemented as a standalone function that belongs to the class.


class MathUtils:
    
    @staticmethod
    def add_numbers(x, y):
        return x + y
    
    @staticmethod
    def multiply_numbers(x, y):
        return x * y


# Calling static methods on the class directly
result1 = MathUtils.add_numbers(5, 3)
print(result1)  # Output: 8

result2 = MathUtils.multiply_numbers(5, 3)
print(result2)  # Output: 15


# In the example above, add_numbers() and multiply_numbers() are static methods defined using the
# @staticmethod decorator. These methods do not have access to the instance or class attributes and behave like regular functions.




#Inheritance in Python

#Base class

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        print("Dog barks")  # Overriding the speak method of the base class

dog1 = Dog("Buddy", "Labrador")
dog1.speak()  # Output: Dog barks



#Abstract base class and Interfaces
 

# Abstract base classes are classes that cannot be instantiated directly 
# but provide a common interface and define a set of 
# methods that derived classes must implement.
#  ABCs are defined using the abc module in Python.


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
class Rectangel(Shape):
    def __init__(self,width,length):
        self.width=width
        self.length=length

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    
shapes = [Circle(5), Rectangel(4,6)]

for shape in shapes:
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())