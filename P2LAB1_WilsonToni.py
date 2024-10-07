# Toni Wilson
# 09-30-2024
# P2LAB1
# Performing Mathematical Calculations

import math
# User input
radius = float(input("What is the radius of the circle? "))
print()

# Caculations
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display results
print(f"The diameter of the circle is {diameter:.1f}")
print()

print(f"The circumference of the circle is {circumference:.2f}")
print()

print(f"The area of the circle is {area:.3f}")
