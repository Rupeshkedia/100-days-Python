try:
    file = open("count.txt", "r")
    count = int(file.read())
    file.close()
except:
    count = 0

count += 1

file = open("count.txt", "w")
file.write(str(count))
file.close()

print("Program executed", count, "times")