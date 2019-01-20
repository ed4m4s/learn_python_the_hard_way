#!/usr/bin/python

# Exercise on IS-A, Has-A, Objects and Classes

## Animal is-a object
class Animal(object):
    pass

## Dog Is-A Animal
class Dog(Animal):

    def __init__(self, name):
        ## Has-A name
        self.name = name

## Cat Is-A Animal
class Cat(Animal):

    def __init__(self, name):
        ## Has-A name
        self.name = name

## Person Is-A object
class Person(object):

    def __init__(self, name):
        ## Has-A name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee Is-A Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Has-A name
        super(Employee, self).__init__(name)    ## SUPER Does not require you to reference the parent OR class names explicitly, which can be handy.
        ## Has-A Salary
        self.salary = salary

## Fish Is-A object
class Fish(object):
    pass

## Salmon Is-A Fish
class Salmon(Fish):
    pass

## Halibut Is-A Fish
class Halibut(Fish):
    pass

## Rover is a Dog
rover = Dog("Rover")
print rover.name

## Satan is a Cat
satan = Cat("Satan")
print satan.name

## Mary is a Person
mary = Person("Mary")
print mary.name

## Mary's Pet is a Satan
mary.pet = satan

## Frank is an Employee and has salary of 120000
frank = Employee("Frank", 120000)
print frank.name, frank.salary

## Frank's pet is a rover
frank.pet = rover


## flipper is a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()