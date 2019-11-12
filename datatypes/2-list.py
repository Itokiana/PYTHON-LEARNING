"""
How to slice lists in Python?
"""
my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])
# elements beginning to 4th
print(my_list[:-5])
# elements 6th to end
print(my_list[5:])
# elements beginning to end
print(my_list[:])

# --------------------------------------------------------------------

"""
How to change or add elements to a list?
"""
# eg1
# mistake values
odd = [2, 4, 6, 8]
# change the 1st item    
odd[0] = 1            
# Output: [1, 4, 6, 8]
print(odd)
# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  
# Output: [1, 3, 5, 7]
print(odd) 

# /////////////////////

# eg2
odd = [1, 3, 5]
odd.append(7)
# Output: [1, 3, 5, 7]
print(odd)
odd.extend([9, 11, 13])
# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)

# //////////////////////

# eg3
odd = [1, 3, 5]
# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])
#Output: ["re", "re", "re"]
print(["re"] * 3)

# //////////////////////

# eg4
odd = [1, 9]
odd.insert(1,3)
# Output: [1, 3, 9] 
print(odd)
odd[2:2] = [5, 7]
# Output: [1, 3, 5, 7, 9]
print(odd)

# --------------------------------------------------------------------

"""
How to delete or remove elements from a list?
"""

# eg 1
my_list = ['p','r','o','b','l','e','m']
# delete one item
del my_list[2]
# Output: ['p', 'r', 'b', 'l', 'e', 'm']     
print(my_list)
# delete multiple items
del my_list[1:5]  
# Output: ['p', 'm']
print(my_list)
# delete entire list
del my_list       
# Error: List not defined
print(my_list)

# //////////////////////

# eg 2
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'o'
print(my_list.pop(1))
# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'm'
print(my_list.pop())
# Output: ['r', 'b', 'l', 'e']
print(my_list)
my_list.clear()
# Output: []
print(my_list)

# --------------------------------------------------------------------

"""
List Comprehension: Elegant way to create new List
"""

pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)

# This code is equivalent to

pow2 = []
for x in range(10):
    pow2.append(2 ** x)

pow2 = [2 ** x for x in range(10) if x > 5] # => [64, 128, 256, 512]
odd = [x for x in range(20) if x % 2 == 1] # => [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
add = [[x+y for x in ['Python ','C '] for y in ['Language','Programming']] # => ['Python Language', 'Python Programming', 'C Language', 'C Programming']


# --------------------------------------------------------------------

"""
Other List Operations in Python
"""

my_list = ['p','r','o','b','l','e','m']
# Output: True
print('p' in my_list)
# Output: False
print('a' in my_list)
# Output: True
print('c' not in my_list)

"""
Iterating Through a List

Using a for loop we can iterate though each item in a list.
"""
for fruit in ['apple','banana','mango']:
    print("I like",fruit)