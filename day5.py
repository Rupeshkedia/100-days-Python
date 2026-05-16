#Print the grade sheet of a student for the given range of cgpa. Scan marks of five
#subjects and calculate the percentage.
sub1 = float(input("enter marks of first subject : "))
sub2 = float(input("enter marks of second subject : "))
sub3 = float(input("enter marks of third subject : "))
sub4 = float(input("enter marks of fourth subject : "))
sub5 = float(input("enter marks of fifth subject : "))
percentage = (sub1+sub2+sub3+sub4+sub5)/5
print("the percentage is:", percentage)
cgpa = percentage/10
print("the cgpa is:", cgpa)
if cgpa>=9.1:
  print("grade o")
elif cgpa>=8.1:
  print("grade A+")
elif cgpa>=7.1:
  print("grade A")
elif cgpa>=6.1:
  print("grade B+")
elif cgpa>=5.1:
  print("grade B")
elif cgpa>=4.1:
  print("grade C")
else:
  print("grade F")