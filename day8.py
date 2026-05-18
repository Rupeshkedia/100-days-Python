num = int(input("enter a number:"))
flag = 0

for i in range(2, num):
  if num % i == 0:
    flag = 1
    break
if flag == 0 and num > 1:
  print("prime number")
else:
  print("not a prime number")