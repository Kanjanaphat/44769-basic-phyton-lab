num = int(input("Enter your loop: "))
numtotal =[]
for i in range(num):
    data = int(input('Enter your data: '))
    numtotal += [data]
    total = sum(numtotal)
print(total)