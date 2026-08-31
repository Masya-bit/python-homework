import math

def square(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area

print(square(6))
print(square(4.2))
print(square(8.1))