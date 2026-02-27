# Input
name = input("Enter student name: ")
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

# total and percentage
total = m1 + m2 + m3
percentage = (total / 300) * 100

# Grade
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Output
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
