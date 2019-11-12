"""
The infinite loop
Example #1: Infinite loop using while
"""

# An example of infinite loop
# press Ctrl + c to exit from the loop
while True:
    num = int(input("Enter an integer: "))
    print("The double of",num,"is",2 * num)


# ---------------------------------------------------------------

"""
Loop with condition at the top
Example #2: Loop with condition at the top
"""

# Program to illustrate a loop with condition at the top

# Try different numbers
n = 10

# Uncomment to get user input
#n = int(input("Enter n: "))

# initialize sum and counter
sum = 0
i = 1

while i <= n:
   sum = sum + i
   i = i+1    # update counter

# print the sum
print("The sum is",sum)

#--------------------------------------------------------------------

"""
Loop with condition in the middle
Example #3: Loop with condition in the middle
"""

# Program to illustrate a loop with condition in the middle. 
# Take input from the user untill a vowel is entered
vowels = "aeiouAEIOU"
# infinite loop
while True:
    v = input("Enter a vowel: ")
    # condition in the middle
    if v in vowels:
        break
    print("That is not a vowel. Try again!")
print("Thank you!")

#--------------------------------------------------------------------

"""
Loop with condition at the bottom
Example #4: Loop with condition at the bottom
"""

# Python program to illustrate a loop with condition at the bottom
# Roll a dice untill user chooses to exit
# import random module
import random
while True:
   input("Press enter to roll the dice")
   # get a number between 1 to 6
   num = random.randint(1,6)
   print("You got",num)
   option = input("Roll again?(y/n) ")
   # condition
   if option == 'n':
       break