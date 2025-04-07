"""Create a Vector class that simulates a 1D vector array. 

Assume the inputs to the class are valid. The Vector instance should be initialized with at least two attributes.

The Vector class should enable adding either an integer or a different vector to a vector.

The Vector class should enable checking which of two vectors is bigger, element-wise. 

The output is another vector with the corresponding True and False values.
    """
from typing import Iterable
class Vector():
    def __init__(self, values: Iterable):
        self.values = list(values)
        self.length = len(self.values)
    def __len__(self):
        """Return the length of the vector."""
        return self.length
    def __str__(self):
        return f"Vector:\t(Values:{self.values}, length: {self.length})"
    def __add__(self, other):
        """Add two vectors or a vector and an integer."""
        if isinstance(other, int):
            return Vector([x + other for x in self.values])
        elif isinstance(other, Vector):
            return Vector([x + y for x, y in zip(self.values, other.values)])
        else:
            raise TypeError("Can only add another Vector or an int")
    def which_is_bigger(self, other: "Vector"):
        return Vector([x > y for x, y in zip(self.values, other.values)])

vec = Vector([1, 2, 3, 4, 5, 6])
print(vec)

vec2 = Vector([5, 4, 3, 2, 1])
vec3 = vec + vec2
vec4 = vec + Vector([0, 8, -2, 5, 0])
print(vec3)
print(vec4)
print(vec3.which_is_bigger(vec4))