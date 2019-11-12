"""
This is nearly the same as

def double(x):
   return x * 2
"""

# Program to show the use of lambda functions

double = lambda x: x * 2

# Output: 10
print(double(5))


# --------------------------------------------------------
"""
Example use with filter()
"""
# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)

# ---------------------------------------------------------
"""
Example use with map()
"""
# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
