

def list_avg(sequence: list) -> float:
  return sum(sequence) / len(sequence)

res = list_avg([1, 2, 3])

class Book:
  pass

def avg_price(seque: list[Book]) -> float:
  pass

# not correct: avg_price expects a list of Book objects
avg_price([1,2,3])
