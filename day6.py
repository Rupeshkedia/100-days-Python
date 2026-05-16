#Write a program which takes any date as input and display next date of the calendar
#e.g.
#I/P: day=20 month=9 year=2005
#O/P: day=21 month=9 year 2005
day = int(input("Enter Date  : "))
month = int(input("Enter Month : "))
year = int(input("Enter year  : "))

jan = 31
feb = 28
march = 31
april = 30
may = 31
june = 30
july = 31
aug = 31
sept = 30
oct = 31
nov = 30
dec = 31

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    feb = 29

HighestDays = 0 # Initialize HighestDays to prevent NameError if month is invalid

if month == 1:
    HighestDays = jan
elif month == 2:
    HighestDays = feb
elif month == 3:
    HighestDays = march
elif month == 4:
    HighestDays = april
elif month == 5:
    HighestDays = may
elif month == 6:
    HighestDays = june
elif month == 7:
    HighestDays = july
elif month == 8:
    HighestDays = aug
elif month == 9:
    HighestDays = sept
elif month == 10:
    HighestDays = oct
elif month == 11:
    HighestDays = nov
elif month == 12:
    HighestDays = dec

# More comprehensive check for invalid date
if day < 1 or day > HighestDays or month < 1 or month > 12:
  print("invalid date, May be your next date is:")
  exit()

day = day + 1


if day > HighestDays:
    day = 1
    month = month + 1

    if month > 12:
        month = 1
        year = year + 1

print("Next Date:")
print("day =", day, "month =", month, "year =", year)