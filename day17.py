#ques 2) Create a tuple to store n numeric values and find average of all values.

n = int(input("Enter number of values: "))
values = []
for i in range(n):
  num = int(input(f"enter value {i+1}: "))
  values.append(num)
value_tuple = tuple(values)
avg = sum(value_tuple) / len(value_tuple)
print(f"Average of values: {avg}")