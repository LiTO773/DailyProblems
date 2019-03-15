def cons(a, b):
  def pair(f):
      return f(a, b)
  return pair

# Returns the first element
def car(pair):
  def find_elem(a, b):
    return a
  return pair(find_elem)

# Returns the last element
def cdr(pair):
  def find_elem(a, b):
    return b
  return pair(find_elem)

print(car(cons(3,4)))
print(cdr(cons(3,4)))