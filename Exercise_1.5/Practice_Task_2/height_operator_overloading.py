class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f"{self.feet} feet, {self.inches} inches"

    def __add__(self, other):
        total_inches_self = self.feet * 12 + self.inches
        total_inches_other = other.feet * 12 + other.inches
        total_inches = total_inches_self + total_inches_other

        feet = total_inches // 12
        inches = total_inches % 12
        return Height(feet, inches)

    def __sub__(self, other):
        total_inches_self = self.feet * 12 + self.inches
        total_inches_other = other.feet * 12 + other.inches
        diff_inches = total_inches_self - total_inches_other

        # Ensure no negative height
        if diff_inches < 0:
            diff_inches = 0

        feet = diff_inches // 12
        inches = diff_inches % 12
        return Height(feet, inches)


# Create Height objects
person_a = Height(5, 10)
person_b = Height(4, 10)
person_c = Height(3, 9)

# Add heights
height_sum = person_a + person_b
print("Total height:", height_sum)

# Subtract heights
height_diff = person_a - person_c
print("Resulting height after subtraction:", height_diff)
