
# LEGB rule

# 1. Local
# 2. Enclosing
# 3. Global
# 5. Built-in

# Local
x = 'global x'
def report():
  x = 'local x'
  print(x)

# report()

# Enclosing

def outer():
  # x = 'outer x'
  def inner():
    # x = 'inner x'
    print(x)
  inner()
  print(x)

outer()

print(__file__)
print(__name__)
