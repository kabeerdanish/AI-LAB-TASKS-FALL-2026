"""1  Home Task 1: Debug the Broken Program Problem statement:  The program below is meant to store a student record and print it, but it fails to run. Copy it, find every error, correct it and add a short comment above each correction explaining what was wrong and why your fix works. 

student = ('Nadeem', 28, 3.75) 
student[1] = 24                       # the student had a birthday 

def show(name, age): 
    print('Name : ', name) 
    print('Age  : ', age) 
    
show(28, 'Nadeem') 

age_entered = input('Enter age: ') 
if age_entered > 18: 
    print('Adult') 
    
marks = [90, 85, 78] 
print('Average : ', total / 3) 

Requirements and constraints: 
• Identify at least four distinct errors and classify each one as a syntax error, a type error, a logical error or a name error. 
• Keep the tuple as a tuple: solve the update problem without converting the record into a list, and explain in a comment why the original line failed. 
• The corrected program must run from top to bottom and print the record, the age check and the correct average. Expected outcome:  A working program plus a comment block listing every error found, its category and the reasoning behind the fix. """



student = ('Nadeem', 28, 3.75) 
# student[1] = 24                       # the student had a birthday 
# student[1] = 24 : it is a type error. The code will run, but will stop at this position. It is an error cuz tuples can not be updated. And here we are updating it. The tuple foes not support item assignment. 

# Solution:
student = ('Nadeem', 24, 3.75)


def show(name, age): 
    print('Name : ', name) 
    print('Age  : ', age) 
    

# show(28, 'Nadeem') # logical error
# We can't give number to a name. The arguments shoud be passed in right manner

# Solution
show("Nadeem", 28)

# age_entered = input('Enter age: ')  # type error
# we should convert string to the int. Otherwise a string of age can't be compared with 18 of int
age_entered = int(input('Enter age: '))
if age_entered > 18: 
    print('Adult') 
    
marks = [90, 85, 78] 
# print('Average : ', total / 3) # Name error : total is not defined
# before deividing total by 3, we have to define and find total. Here we don't know what total is.
total = 0
for i in marks:
    total+=i
print('Average : ', total / 3)