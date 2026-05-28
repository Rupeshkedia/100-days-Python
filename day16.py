s = input("enter a string: ")
s = s.upper()

letters = {}

for ch in s:
  if ch.isalpha():
    letters[ch] = letters.get(ch,0) + 1

for key in sorted(letters):
  print(letters[key],key)