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

# WORKING WITH PART OF A LIST
print("\n\t\tSLICING A LIST")
players = ['charles', 'martina', 'michael','florence','eli']
print(players[0:3]) # prints a slice of this list.
print("Here are the first three players on my team:")
for player in players[:3]: # Instead of looping through the entire list of players.
    # python loops through only the first three names.
    # for loop through a subset of the elements in a list.
    print(player.title())



# COPYING A LIST
print("\n\t\tCOPYING A LIST")
my_foods = ['pizza', 'falafel','carrot cake'] # created a list called my_foods
friend_foods = my_foods[:] # make a copy to this new list without specifying any indices.

my_foods.append('cannoli') #Added new foods to each list
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


