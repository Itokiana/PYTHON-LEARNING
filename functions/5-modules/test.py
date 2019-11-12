import module

print(module.add(4,5.5))

# --------------------------------------------------------

# import statement example
# to import standard module math

import math
print("The value of pi is", math.pi)

# --------------------------------------------------------

# import module by renaming it

import math as m
print("The value of pi is", m.pi)

# --------------------------------------------------------

# import only pi from math module

from math import pi
print("The value of pi is", pi)


# --------------------------------------------------------

# import all names from the standard module math

from math import *
print("The value of pi is", pi)

# --------------------------------------------------------

# Python Module Search Path
"""
While importing a module, Python looks at several places. Interpreter first looks for a built-in module then (if not found) into a list of directories defined in sys.path. The search is in this order.

    The current directory.
    PYTHONPATH (an environment variable with a list of directory).
    The installation-dependent default directory.

"""

import sys
print(sys.path)

# --------------------------------------------------------