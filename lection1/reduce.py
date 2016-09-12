from functools import reduce
a = [1,2,3]

# -- functional --
b = 0
b = reduce((lambda x, y: x + y), a)
print(b)

# -- algorithmical --
b = 0
for num in a:
    b += num
print(b)