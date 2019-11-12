import os

"""
Get Current Directory
"""
print(os.getcwd())

# -----------------------------------------

"""
Changing Directory
"""

os.chdir("/home/itokiana/PROJET/LABS/PYTHON/BASE/lesson")
print(os.getcwd())

# -----------------------------------------

"""
List Directories and Files
"""

print(os.listdir(os.getcwd()))