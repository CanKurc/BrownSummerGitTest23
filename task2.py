mintoHour = False;
while True:
    x = input("Type h for minutes to hours, m for hours to minutes: \n")
    if (x == "h"):
        mintoHour = True
        break
    elif (x == "m"):
        mintoHour = False
        break

var = 0
while True:
    x = input("Enter the amount as an int: \n")
    if x.isnumeric():
        var = x
        break

if (mintoHour):
    print(int(int(var) / 60))
else:
    print(int(int(var) * 60))