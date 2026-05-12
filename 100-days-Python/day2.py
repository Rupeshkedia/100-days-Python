#Find the greatest among the two numbers. If numbers are equal than print “numbers are
#equal”.
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
if num1>num2:
  print(f"{num1} is greater than {num2}")
if num2>num1:
  print(f"{num2} is greater than {num1}")
else:
  print("both number are equal")