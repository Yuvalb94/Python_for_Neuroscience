from __future__ import annotations

# Introducing the class keyword:
class Point:
    """Represents a point in a 2D space."""  
    def __init__(self, x=0, y=0):
        """
        Initialize a new Point instance.

        Parameters
        ----------
        x : float
            X-axis coordinate
        y : float
            Y-axis coordinate
        """        
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def calculate_distance(self, other : Point):
        """Calculate the distance to another point."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    def __add__(self, other: Point):
        """Add two points."""
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other: Point):
        """Subtract two points."""
        return Point(self.x - other.x, self.y - other.y)
    pass


# A new type is born in __main__
blank = Point(1,2)

blank2 = Point(3,4)
print(blank)

# print(calculate_distance(blank, blank2))
print(blank.calculate_distance(blank2))

blank3 = blank + blank2
print(blank3)
