"""
Advantages of Recursion

    Recursive functions make the code look clean and elegant.
    A complex task can be broken down into simpler sub-problems using recursion.
    Sequence generation is easier with recursion than using some nested iteration.

Disadvantages of Recursion

    Sometimes the logic behind recursion is hard to follow through.
    Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
    Recursive functions are hard to debug.

"""



# An example of a recursive function to
# find the factorial of a number

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))	