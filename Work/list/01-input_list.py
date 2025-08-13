num = int(input("Enter your loop: "))
numtotal =[]
for i in range(num):
    data = int(input('Enter your data: '))
    numtotal += [data]
if num % 10 == 0:
    numtotal.append(num)
print(numtotal)