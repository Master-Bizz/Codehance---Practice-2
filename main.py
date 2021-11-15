"""
Variable Assignment
"""

name = "Welcome again MAster Biz"
#print(name)

# Multiple Variables on the same line
a = b = c = "repetition\nis\nthe game"
print(a)
print(b)
print(c)

#careful not to over-ride your variables
colour = "blue"
colour = "cool"
print(colour)

# Anything can be used or set as variable names but there are: Illegal Variable names examples;
#2colours ="blue"
#2 colours = "blue"
#2-colours = "blue"

"""
Reserved Keys Words
"""
# help("keywords")
print("Go to shell and type python and then type; 'help{keywords}")

"""
Variable Types
"""
var = "boom"
print(type(var))
# String
var = 223
print(type(var))
# Integer

"""
Object Identity
"""
#score = 3678
#print(id(score))

#score = 786
#pb = score
#print(id(score))
#print(id(pb))

"""
Object reference
"""
# score = 100
#pb = score
#print(type(score))
#print(type(pb))
#print(score)
#rint(pb)
# Both Score and pb point to the same int object
# score-----> int 100 <------pb

score = "completed"
score = 100
pb = 20
print(type(score))
print(type(pb))
print(score)
print(pb)