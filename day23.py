d = {
    "a": 10,
    "b": 10,
    "c": 10
}

same = (lambda x: len(set(x.values())) == 1)(d)

if same:
    print("All values are same")
else:
    print("All values are not same")