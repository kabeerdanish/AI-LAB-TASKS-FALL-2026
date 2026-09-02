def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def digit_sum(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total

def classify(n, threshold=100):
    if n < threshold:
        return "small"
    else:
        return "large"

def summarise(*numbers):
    smallest = numbers[0]
    largest = numbers[0]
    total = 0
    count = 0
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
        total = total + number
        count = count + 1
    average = total / count
    return {
        "smallest": smallest,
        "largest": largest,
        "average": average
    }

def describe(**details):
    for key, value in details.items():
        print(key, ":", value)


print("\nNUMBER TOOLKIT\n")
print("Prime numbers from 1 to 20:")

for number in range(1, 21):
    if is_prime(number):
        print(number, end=" ")

print()
print("Digit sum of 28:", digit_sum(28))
print("Digit sum of 125:", digit_sum(125))
print("Classify 80 with threshold 100:", classify(80, 100))
print("Classify 80 with default threshold:", classify(80))
print("Classify 150 with keyword:", classify(150, threshold=100))

result = summarise(45, 80, 120, 60, 95)
print("Summary:", result)
print("Student Details:")
describe(name="Nadeem", age=28)
