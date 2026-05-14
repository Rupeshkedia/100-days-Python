#Find whether a given year is a leap year or not.
year = int(input("enter a year"))
if(year % 4 == 0 and year % 100 != 0) or (year %400 == 0):
  print("it is a leap year")
else:
  print("it is not a leap year")