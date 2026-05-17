n = int(input("Enter a number: "))
length = len(str(n))
sum = 0
temp = n
while temp > 0:
  digit = temp % 10
  sum = sum + digit ** length
  temp = temp // 10

if sum==n:
  print("Armstrong number")
else:
  print("Not armstrong")