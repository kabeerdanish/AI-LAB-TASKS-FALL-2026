sentence = input("Enter a sentence: ")
vowels = 0
consonants = 0
unique_chars = set()
frequency = {}

for char in sentence:
    if char != " ":
        unique_chars.add(char)
        if char.lower() in "aeiou":
            vowels = vowels + 1
        elif char.isalpha():
            consonants = consonants + 1
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1

reverse = ""
i = len(sentence) - 1
while i >= 0:
    reverse = reverse + sentence[i]
    i = i - 1

print("\nTEXT ANALYSER")

print("Vowels:", vowels)

print("Consonants:", consonants)

print("Unique characters:", unique_chars)

print("Number of unique characters:", len(unique_chars))

print("\nRepeated characters:")
for char in frequency:
    if frequency[char] > 1:
        print(char, ":", frequency[char])

print("Reversed sentence:", reverse)
print("First five characters:", sentence[:5])
print("Last five characters:", sentence[-5:])
