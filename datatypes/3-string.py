"""
String Membership Test
"""

print('a' in 'program')
print('at' not in 'battle')

# ----------------------------------------------------------------

"""
Built-in functions to Work with Python
"""
str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))

# ----------------------------------------------------------------

"""
Escape sequence
"""

# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")

# ----------------------------------------------------------------

"""
Common Python String Methods
"""
print("PrOgRaMiZ".lower())
print("PrOgRaMiZ".upper())
print("This will split all words into a list".split())
print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))
print('Happy New Year'.find('ew'))
print('Happy New Year'.replace('Happy','Brilliant'))