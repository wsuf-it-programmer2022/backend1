
# snake_case instead of camelCase
# boolean type: True or False
user_logged_in = True

# we are using indentation instead of curly braces to define blocks
if user_logged_in == True:
  # this is inside the if block
  print('Welcome!')

# this is outside the if block
print('hello wolrd')
# double quotes and single quotes are the same
print("hello wolrd")

# in python indentation is very important
num = 10
while num > 0:
  # f string: template string, in javascript: `num is ${num}`
  print(f'num is {num}')
  num = num - 1

# range(10) is a function that returns a list of numbers from 0 to 9
# we are converting the range to a list
print(list(range(10)))

for num in range(10):
  print(f'num is {num}')

# creating a function

def say_hello(name):
  print(f'hello {name}')

say_hello('John')

# creating a list
my_names = ['John', 'Mary', 'Bob']
print(my_names)
print(type(my_names))

my_names.append('Alice')

print(my_names)

my_names.__delitem__(1)

print(my_names)

my_names.remove('Bob')

print(my_names)

# accessing the first element of the list
print(my_names[0])

# this item does not exist so we get an error
# print(my_names[3])

# access the last item of the list
print(my_names[-1])
# in javascript we would access the last element like:  my_names[my_names.length - 1]


# when creating a range, the first number is inclusive and the last number is exclusive
print(list(range(1,11)))

numbers = list(range(1,11))

# print the first 3 elements of the list, from 0 to 2
print(numbers[0:3])

# lower bound, upper bound:
# from zero to 3
print(numbers[:3])
# from 3 to the end
print(numbers[3:])

# tuple variable: a list that cannot be modified
my_tuple = (1,2,3)
print(my_tuple)

# set: a list that does not allow duplicates
my_set = {1,2,3,3,3,3,3,3,3,3,3,3,3,3,3}
print(my_set)

my_list = [1,2,3,3,3,3,3,3,3,3,3,3,3,3,3]
print(my_list)
my_list_without_duplicates = list(set(my_list))
print(my_list_without_duplicates)

# dictionary: a list of key value pairs
my_dict = {
  'name': 'John',
  'age': 30,
  'is_logged_in': True
}

my_dict['data'] = [1,2,3,4, [ 1,2,3,4,5 ], (23,3), {'test': 'hello'} ]

print(my_dict)
print(my_dict['name'])
print(my_dict['data'][4][2])


# type hinting

def add(a: int, b: int) -> int:
  return a + b

my_list: list = [1,2,3,4,5]

def say_hello(name: str, x=10, y=10) -> str:
  """
  This function says hello to the user
  @param name: the name of the user
  @return: a string
  """
  return f'Hello {name}'

multi_line_string = """
  This is a multi line string
  This is the second line
  This is the third line
"""

# positional arguments
print(say_hello('John', 1, 2))
# keyword arguments are optional
print(say_hello(x=1, y=2, name='John'))

print(say_hello('John'))
# error: 
# print(say_hello('John', 3,4,5))


# built-in global variables
print(__file__)

