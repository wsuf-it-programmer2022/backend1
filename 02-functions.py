

# Functions are defined using the def keyword
# this is an empty function
def my_first_function():
  pass

def add_user(users, new_user):
  users.append(new_user)

users: list = ['John', 'Mary', 'Bob']

# lists are passed by reference
add_user(users, 'Alice')
print(users)


def set_name(name, new_name):
  name = new_name

# strings are passed by value
name: str = 'John'
set_name(name, 'Alice')

print(name)

# in general scalars (strings, numbers, etc..) are passed by value and
# collections (lists, dictionaries) are pased by reference 

vehicle: str = 'car'

def drive():
  global vehicle
  vehicle = vehicle.upper()
  print(vehicle)

drive()

def divide(divided, divisor=2):
  if divisor == 0:
    return None
  return divided / divisor

result = divide(10, 2)
print(result)
result = divide(10)


# anonymous functions = lambda functions
seq = [1, 2, 3, 4, 5]
def times2(x):
  return x * 2

# these two are equivalent
result = map(times2, seq)
result = map(lambda x: x * 2, seq)
print(list(result))

# rest parameter: *args
# args is a tuple, it can be named anything
# the multiply function takes any number of arguments and multiplies them
def multiply(*args):
  result = 1
  print(args)
  print(type(args))
  for arg in args:
    result *= arg
  return result

print(multiply(1, 2, 5))

# keyword arguments
def print_user(name, age, city):
  print(f'Name: {name}, Age: {age} City: {city}')

# positional arguments
print_user('John', 30, 'London')
# this is equivalent to the above 
# keyword arguments can be passed in any order
# keyword arguments must come after positional arguments 
print_user('John', age=30, city='London')

# rest keyword arguments: **kwargs
def print_user2(person, **kwargs):
  print(person)
  print(kwargs)
  print(type(kwargs))
  for key, value in kwargs.items():
    print(f'{key}: {value}')

print_user2('John', age=30, city='London', country='UK')

my_nums = [1, 2, 3, 4, 5]
print(my_nums)
# unpacking a list ( in javascript this is called spreading)
print(*my_nums)

def my_function():
  num_list = []
  for num in range (1, 10000000):
    num_list.append(num)
  print("the sum is: ", sum(num_list))

import time
import functools

def timing_function(callback):
  # we use functools.wraps to preserve the name of the function
  @functools.wraps(callback)
  def wrapper():
    start_time = time.time()
    callback()
    end_time = time.time()
    print(f'it took {end_time - start_time} seconds')
  return wrapper

# decorator = a function that takes a function as an argument and returns a function
# we are adding functionality to my_function without modifying it
wrapped_function = timing_function(my_function)
wrapped_function()

@timing_function
def my_sum():
  num_list = []
  for num in range (1, 10000000):
    num_list.append(num)
  print("the sum is: ", sum(num_list))


my_sum()
print(my_sum.__name__)


x = [ 1, 2, 3, 4, 5 ]
out = []
for item in x:
  out.append(item**2)
print(out)

# the same with list comprehension
out = [ item**2 for item in x ]
print(out)

users = [('John', 30), ('Mary', 25), ('Bob', 40)]

user_mapping = {}
for user in users:
  user_mapping[user[0]] = user[1]
print(user_mapping)

# the same with dictionary comprehension
user_mapping = { user[0]: user[1] for user in users }
print(user_mapping)

