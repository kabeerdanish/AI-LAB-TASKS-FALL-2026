def triangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

def multiplication_table(*numbers):
    for num in numbers:
        print(f"Table of {num}:")
        for i in range(1,11):
            print(f"{num} x {i} = {num*i}")
        print()

def fibonacci(limit):
    a= 0
    b=1
    fib_lis=[]
    while a < limit:
        fib_lis.append(a)
        a=b, 
        b=a+b
    return fib_lis

def collatz(n):
    steps=0
    while n != 1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        steps+=1
    return steps


print("1. Triangle Pattern:")
triangle(5)

print("\n2. Multiplication Tables:")
multiplication_table(2, 5, 7)

print("\n3. Fibonacci Series:")
fib_res = fibonacci(50)
print(fib_res)

print("\n4. Collatz Steps:")
collatz_steps = collatz(27)
print("Steps taken for 27:", collatz_steps)