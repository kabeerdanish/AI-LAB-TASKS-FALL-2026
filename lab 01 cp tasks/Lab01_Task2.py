results = [
    ("AI", 88),
    ("Programming", 76),
    ("Database", 65),
    ("English", 55),
    ("Maths", 45),
    ("SE", 72),
]

grades = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}

invalid = 0
total = 0
count = 0

print("\nSEMESTER RESULT")
for subject, marks in results:
    if marks < 0 or marks > 100:
        invalid = invalid + 1
        continue
    if marks >= 85:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    grades[grade] = grades[grade] + 1
    total = total + marks
    count = count + 1
    print(subject, ":", marks, "->", grade)

average = total / count

print("\nGRADE SUMMARY")
print(grades)
print("Invalid entries:", invalid)
print("Average marks:", average)
