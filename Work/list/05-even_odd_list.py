num = int(input("Enter your loop: "))
odd = []; even = []
for i in range (num):
    number = int(input("Enter your data: "))
    if ((number % 2)==0):
        even.append(number)
    else:
        odd.append(number)
print(odd)
print(even)