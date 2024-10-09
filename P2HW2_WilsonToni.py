# Toni Wilson
# 10-09-2024
# P2HW2
# Display grades

grades = []

module_1 = float(input("Enter grade for Module 1: "))
module_2 = float(input("Enter grade for Module 2: "))
module_3 = float(input("Enter grade for Module 3: "))
module_4 = float(input("Enter grade for Module 4: "))
module_5 = float(input("Enter grade for Module 5: "))
module_6 = float(input("Enter grade for Module 6: "))

grades.append(module_1)
grades.append(module_2)
grades.append(module_3)
grades.append(module_4)
grades.append(module_5)
grades.append(module_6)

print()
print("-------------------Results-------------------")
print()
average = (sum(grades)//len(grades))

print(f"{'Lowest Grade:':<18}{min(grades):<25}")
print(f"{'Highest Grade:':<18}{max(grades):<25}")
print(f"{'Sum of Grades:':<18}{sum(grades):<25}")
print(f"{'Average:':<18}{average:<25,.2f}")
