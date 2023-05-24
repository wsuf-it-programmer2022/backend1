

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
