print("Hello Again")
"""
Text Type - string
"""
# s = "string"
# print(s)
# print(type(s))
# ---------------------------
# m = """A multiple line string"""
# print(m)
# print(type(m))
# ---------------------------
# Indexing
# i = "index"
# print(i[4])
# l = "longer sample"
# print(l[1:5])
# Shows character 1 - 5: Begins from Zero (0) Remember!
# ---------------------------
# A string is immutable when you can change/edit string values.
# l = "longer sample"
# l[4] = '9'
# print(l)
# ---------------------------
'''
Numeric Types (Integer, Float, Complex)
'''
x = 234891576
print(type(x))
print("Whole number are Integers and decimal numbers are Float")
f = 8.234786
print(type(f))
# Float is accurate up to 15-16 decimal places.
# ---------------------------
c = 3+3j
print(type(c))
print("Complex numbers involve dealing with imaginary numbers, 'j' in this case")
'''
Sequence Type (List, Tuple, Range)
'''
# List
l = []
l = [3, 2.8, 'coolio']
print(l[2])
# Same rules apply from Indexing (starting from Zero)
print(l[0:3])

# Mutable - Lists can be changed/altered
l[2] = 'Pythonaeus'
print(l)
# ---------------------------
# Tuple - The comma is what makes the class Tuple, without it makes it a string
tuple = ()
# tuple = "yo",
# tuple = ("yo"),
# print(type(tuple))

# tuple = ("dragon, [4,2,1], (1,2,3)")
# print(tuple[8])

# Immutable - Cannot be changes/altered
# tuple = ("dragon, [4,2,1], (1,2,3)")
# tuple[8] = 3
# print(tuple)
# ---------------------------
# Range
# x = range(10)
# for n in x:
  # print(x)
'''
Mapping Type (Dictionary)
'''
# dict = {}
# print(type(dict))
dict = {'name': 'Liam', 'age':27}
print(dict['age'])
print(dict.get('age'))
# changing age
dict['age'] = 28
print(dict)
'''
Set Types (Like Dictionary, but has single values)
'''
# set = {1,2,3}
# set = set() - is an empty set
# set = {} - is an empty dictonary instead
# print(type(set))
# Mixed data types and all immutable
# set = {4.2, "yo", (1,2,3)}
# print(type(set))
# Doesn't register duplicates
# set = {4.2, "yo", (1,2,3), "yo"}
# print(set)
# set = {4.2, "yo", (1,2,3),[1,2,3]}
# print(set)
# TypeError: unhashable type: 'list'
# Cannot have multiple/duplicate lists in a set
'''
Boolean Type (True or False)
'''
print(type(True))
# Boolean as numbers
print(True == 1)
print(False == 0)
# Cool Logic
print(True + True)
print(False + False)
print(True + False)
# Not Boolean operators
print(not False)
print(not True)
# And Boolean operators
print(True and False)
print(False and True)
print(False and False)
# Or Boolean operators
print(True or False)
print(True or True)
print(False or True)
