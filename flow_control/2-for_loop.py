
# PYTHON FOR LOOP

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)

# -------------------------------------------------------------------------

# THE range() FUNCTION
"""
We can generate a sequence of numbers using range() function. 
range(10) will generate numbers from 0 to 9 (10 numbers).
"""

print(range(10))

# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])


# -------------------------------------------------------------------------

# for loop WITH else

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

# -------------------------------------------------------------------------

