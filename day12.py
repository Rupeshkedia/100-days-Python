#11
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
  sum += 1/i
print(f"Total sum is: {sum:.3f}")