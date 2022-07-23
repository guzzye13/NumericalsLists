for value in range(1,6): # range() makes it easy to generate a series of numbers.
    print(value) # prints 1, 2, 3, 4, 5


# Using range() to make a list of numbers
# I can convert the results of range() directly into a list using the list() function.
numbers = list(range(1,6))
print("\nList:", numbers)


# Using range() to tell python to skip numbers in a given range.
even_numbers = list(range(2,11,2)) # starts with value 2 and adds 2 to that value
# stops once it reaches 11
# range(start,stop,step)
print("Even numbers:", even_numbers)


# Using range() to square an integer
squares = [] # empty list called squares
for value in range(1,11): # loop through from 1,10
    square = value ** 2 # current value is raised to the second power and stored in the variable square.
    squares.append(square) # each new value of square is appended to the list of squares.
print("Squared numbers:", squares) # Once loop is finished running, the list of squares is printed.


# A few python functions specific to lists of numbers
digits = [1,3,5,6,7,0]
print("\nDigits:",digits)
print("Minimum:", min(digits))
print("Maximum:", max(digits))
print("Sum:", sum(digits))


