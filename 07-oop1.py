# python is an object oriented programming language
# class is a blueprint for creating objects


class Animal:
  alive = True

  # constructor: a function that gets called when you create an object
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def eat(self):
    print(f'{self.name} is eating')

  def die(self):
    print('Dying...')
    # the class variable is shared by all instances of the class
    Animal.alive = False

  # this is a magic method that gets called when you print an object
  def __str__(self):
    return f'{self.name} is {self.age} years old'

# instantiate an object
my_animal = Animal('Rolf', 10)
my_animal2 = Animal('Bob', 5)
print(my_animal)
my_animal.eat()
my_animal.die()
print(my_animal.alive)
print(my_animal2.alive)


class Dog(Animal):
  def __init__(self, name, age, breed):
    # super() is a reference to the parent class
    super().__init__(name, age)
    self.breed = breed

  def bark(self):
    print('Woof!')


  def __str__(self):
    animal_str = super().__str__()
    return f'{animal_str} and is a {self.breed}'


my_dog = Dog('Rex', 10, 'Labrador')
my_dog.bark()
my_dog.eat()
print(my_dog.breed)
print(my_dog)

print(Dog.__bases__)
print(Dog.__subclasses__())
print(Dog.__mro__)

# multiple inheritance
class A:
  def __init__(self):
    print('A')
  def a(self):
    print('a')

class B:
  def __init__(self):
    print('B')
  def b(self):
    print('b')

class C(A, B):
  def __init__(self):
    print('C')
  def c(self):
    print('c')


my_c = C()
my_c.a()
my_c.b()
my_c.c()

# Object composition

class BookShelf:
  def __init__(self, *books):
    self.books = books

  def __str__(self):
    return f'BookShelf with {len(self.books)} books.'


class Book:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f'Book {self.name}'

book1 = Book('Harry Potter')
book2 = Book('Python 101')

my_bookshelf = BookShelf(book1, book2)
print(my_bookshelf)
# object composition is when you use objects as attributes of other objects
print(my_bookshelf.books)


# static method, and class methods
class Date:
  def __init__(self, date):
    self.date = date
  
  def get_date(self):
    return self.date
 
  # a static method is a method that doesn't use the class or instance
  @staticmethod
  def to_dash_date(date):
    return date.replace('/', '-')
  
  # a class method is a method that uses the class instead of the instance
  @classmethod
  def extra_year(cls, date):
    date_parts = date.split('-')
    year = date_parts[0]
    month = date_parts[1]
    day = date_parts[2]
    new_date = f'{int(year)+1}-{month}-{day}'
    return cls(new_date)


date = Date('2020-01-01')
# I have a separate datestring with different format:
date_string = '2022/01/20'

# I want to create a new Date object from this string, but I want to have the dates
# in the same format

new_date = Date(Date.to_dash_date(date_string))


print(date.get_date())
print(new_date.get_date())

my_date_2 = Date.extra_year("2025-01-01")
print(my_date_2.get_date())
