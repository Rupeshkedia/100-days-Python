text = input("Enter a sentence: ")
count = 0

for char in text:
    if char.isupper():
        count += 1

print(f"Total capital letters: {count}")