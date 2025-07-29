class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    def __str__(self):
        return f"{self.feet} feet, {self.inches} inches"
    
    def __lt__(self, other):
        return (self.feet * 12 + self.inches) < (other.feet * 12 + other.inches)

    def __le__(self, other):
        return (self.feet * 12 + self.inches) <= (other.feet * 12 + other.inches)

    def __eq__(self, other):
        return (self.feet * 12 + self.inches) == (other.feet * 12 + other.inches)

    def __gt__(self, other):
        return (self.feet * 12 + self.inches) > (other.feet * 12 + other.inches)

    def __ge__(self, other):
        return (self.feet * 12 + self.inches) >= (other.feet * 12 + other.inches)

    def __ne__(self, other):
        return (self.feet * 12 + self.inches) != (other.feet * 12 + other.inches)


# Test cases for comparison operators
print("Testing comparison operators:")
print("Height(4, 6) > Height(4, 5):", Height(4, 6) > Height(4, 5))       # True
print("Height(4, 5) >= Height(4, 5):", Height(4, 5) >= Height(4, 5))     # True
print("Height(5, 9) != Height(5, 10):", Height(5, 9) != Height(5, 10))   # True
print()

# Create multiple Height objects
height_1 = Height(4, 10)
height_2 = Height(5, 6)
height_3 = Height(7, 1)
height_4 = Height(5, 5)
height_5 = Height(6, 7)
height_6 = Height(5, 6)

# List of heights
heights = [height_1, height_2, height_3, height_4, height_5, height_6]

# Sort heights using the overloaded operators
sorted_heights = sorted(heights)

# Print sorted heights
print("Sorted heights (ascending):")
for h in sorted_heights:
    print(h)
