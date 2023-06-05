

def my_func():
  my_func()

# this will throw a RecursionError
# my_func()

def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n-1)
    # return 5 * fact(4)
    # return 5 * 4 * fact(3)
    # return 5 * 4 * 3 * fact(2)
    # return 5 * 4 * 3 * 2 * fact(1)
    # return 5 * 4 * 3 * 2 * 1

# 5! = 5 * 4 * 3 * 2 * 1
print(fact(5))
