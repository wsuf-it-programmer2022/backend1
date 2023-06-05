def divide(a,b):
  if b == 0:
    raise ZeroDivisionError("Can't divide by zero")
  return a / b

# print(divide(1,0))

# grades = [23, 45, 67, 89]

grades = []
print('Welcome to the average grade program')
try:
  average = divide(sum(grades), len(grades))
  print(f'The average grade is {average}')
except ZeroDivisionError as e:
  print(e)
  print('There are no grades yet in your list.')
# finally block will always run
finally:
  print('Thank you for using the average grade program.')

print('End of program')
