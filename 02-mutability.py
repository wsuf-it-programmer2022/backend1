

a = []
b = a

# id function returns the memory address of the object
print(id(a))
print(id(b))
c = a.copy()
print(id(c))

# a and b are pointing to the same object
# if we change the object, both a and b will be affected
a.append(35)
print(b)

a = []
b = []

# a and b are pointing to different objects because we created a new list
print(id(a))
print(id(b))

# if we are working with immutable objects, we don't have to worry about this
# because we can't change the object, we can only reassign it

a = 23
b = a

print(id(a))
print(id(b))
b = 24
print(a)

# immutable objects: int, float, bool, string, tuple, range, frozenset
# mutable objects: list, dict, set, bytearray, user-defined classes
