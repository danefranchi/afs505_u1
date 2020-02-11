## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(objext):
   pass

## is-a
class Dog(Animal):

   def__init__(self, name):
      ## has-a
      self.name = name

## is-a
class Cat(Animal):

   def __init__(self, name):
      ## has-a
      self.name = name

## is-a
class Person(object):

   def __init__(self, name):
      ## has-a
      self.name = name

      ## Person has-a pet of some kind
      self.pet = None

## is-a
class Employee(Person):

   def __init__(self, name, salary):
      ## has-a hmm what is this strange magic?
      super(Emplyee, self) __init__(name)
      ## has-a
      self.salary = salary

## is-a
class Fish(object):
   pass

## is-a
class Salmon(Fish):
   pass

## iss-a
class Halibut(Fish):
   pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## has-a
mary.pet = satan

## has-a
frank = Emplyee("Frank", 120000)

## has-a
frank.pet = rover

## has-a
flipper = Fish()

## has-a
crouse = Salmon()

## has-a
harry = Halibut()
