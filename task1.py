var = 0
while True:
    x = input("Enter the amount of hours as an int: \n")
    if x.isnumeric():
        var = x
        break
res = int(var) * 60
print(res)