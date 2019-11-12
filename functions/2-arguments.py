def greet(name,msg):
   """This function greets to
   the person with the provided message"""
   print("Hello",name + ', ' + msg)

greet("Monica","Good morning!")

# ------------------------------------------------------

def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")

# -------------------------------------------------------

def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")

# -------------------------------------------------------