age = int(input())

if (age < 13):
    price = 100
elif (age == 13):
    price = 180
elif (age <= 60):
    price = 180
else:
    price = 120


day = int(input())

if (day == 1):
    day = "monday"

if (day <= 5):
    print (price) 
elif(day >= 5):
    print (price + 50)
else:
    print ("Error")
