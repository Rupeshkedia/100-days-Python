vowels = "aeiouAEIOU"
text = input("Enter a sentence: ")
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Total vowels: {count}")

