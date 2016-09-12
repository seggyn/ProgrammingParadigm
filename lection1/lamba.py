a = 7

# -- functional 1 --
mul = lambda x: x*5
b = 7 if a == 5 else mul(a)
print(b)

# -- functional 2 --
b = 7 if a == 5 else (lambda x: x*5)(a)
print(b)

# -- algorithmical --
def mul(x):
    return x*5
if a == 5:
    b = 7
else:
    b = mul(a)
print(b)