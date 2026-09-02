name = input("Enter name: ")
age = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))

student = {
    "name": name,
    "age": age,
    "cgpa": cgpa,
    "courses": []
}

for i in range(0,3):
    student["courses"].append(input(f"Enter course{i} name: "))

print("\nSTUDENT PROFILE")
print(student)

initials = name[0]
for i in range(len(name)):
    if name[i] == " ":
    initials = initials + name[i + 1]

print("Initials:", initials)

print("\nTYPE REPORT")
for key, value in student.items():
    print(key, ":", value, "->", type(value))

