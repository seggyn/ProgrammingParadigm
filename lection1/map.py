array = [1, 2, 3]

# -- functional --
points = [val*6 for val in array]
print(points)

# -- algorithmical --
points = []
for val in array:
    points.append(val*6)
print(points)