# Wilson Toni
# 10-23-2024
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

print()
print("-------------------Results-------------------")
print()

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = (sum(grades)/len(grades))

print(f"{'Lowest grade: ':<18}{low:<25}")
print(f"{'Highest grade: ':<18}{high:<25}")
print(f"{'Sum of grades: ':<18}{total:<25}")
print(f"{'Average grade: ':<18}{avg:<25,.2f}")
print()
print("---------------------------------------------")
print()
# determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')





