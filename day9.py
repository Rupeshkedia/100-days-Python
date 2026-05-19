#Ques 5 palindrome number
n=int(input("Enter a number: "))
length = len(str(n))
sum = 0
temp = n
while temp>0:
  digit = temp%10
  sum = sum + digit**length
  temp//=10
if sum==n:
  print("Palindrome number")
else:
  print("Not a palindrome number")