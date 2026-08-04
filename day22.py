p = float(input("Entre marks of physics:"))
c = float(input("Enter marks of chemistary:"))
m = float(input("Entre marks of maths:"))
s = p + c + m
a = s/3
if (a>80):
    print("Merit , Sum = ", s , "Average = ", a)
elif (a>70 and a<79.9999):
    print("First Position , Sum = " , s ,"Average = " , a )
elif (a>60 and a<69.999):
    print("Second Position , Sum = " , s , "Average = " , a)
elif (a>50 and a<59.999):
    print("Third Position , Sum = ", s , "Averagae = " , a)
elif (a>40 and a<49.999):
    print("pass , Sum = " , s , "Average = " , a)
else:
    print("Fail , Sum  = " , s , "Average = " , a)
    