#Check whether the quadratic equation has real roots or imaginary roots. Display the
#roots.
a = float(input("enter a number"))
b = float(input("enter a number"))
c = float(input("enter a number"))
d = b**2 - 4*a*c
if d>=0:
  print("real roots")
else:
  print("imaginary roots")
root1 = (-b+d**0.5)/(2*a)
root2 = (-b-d**0.5)/(2*a)
print(f"the roots are{root1} and {root2}")