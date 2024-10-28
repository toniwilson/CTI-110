# Wilson Toni
# 10-23-2024
# P3HW2
# Calculate reg and OT pay for an employee

employee_name = input("Enter employee's name: ")
hours_worked = int(input("Enter number of hours worked: "))
reg_payrate = float(input("Enter employee's pay rate: "))

print()
print("--------------------------------------------------")
print()
print(f"Employee name: {employee_name}")
print()

# OT calculation
overtime_hours = 0
overtime_pay = 0
overtime_payrate = 1.5
reg_hours_pay = 0
gross_pay = 0

reg_hours_pay = (40 * reg_payrate)
ovetime_pay = (overtime_hours * overtime_payrate)
overtime_payrate = (reg_payrate * 1.5)
gross_pay = (reg_hours_pay + ovetime_pay)

if hours_worked > 40:
    overtime_hours = (hours_worked - 40)
    regular_hours = 40

else:
    regular_hours = hours_worked
    reg_hours_pay = (hours_worked * 40)
    gross_pay = (reg_hours_pay + 0)

# Display results
print(f"Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("---------------------------------------------------------------------------------")
print(f"{hours_worked:<15.2f}{reg_payrate:<15.2f}{overtime_hours:<15.2f}{overtime_pay:<15.2f}{regular_hours:<15.2f}{gross_pay:<15.2f}")

