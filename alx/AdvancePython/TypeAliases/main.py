from typing import TypeAlias, NewType
Vector: TypeAlias = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(3.0, [1.0, -4.2, 5.4])
print(new_vector)
