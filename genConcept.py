# Generator Function
def my_generator(): 
  yield 1 
  yield 2 
  yield 3 
gen = my_generator() 
print(next(gen)) # Output: 1 
print(next(gen)) # Output: 2 
print(next(gen)) # Output: 3

# Generator Expressions
gen = (x * x for x in range(3))
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 4

