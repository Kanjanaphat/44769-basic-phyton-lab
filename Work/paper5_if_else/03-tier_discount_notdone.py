price = float(input())

if(price <= 500):
    print (price)
elif(price >= 500 and price < 1000):
    print (price - (price * 5 / 100))
elif(price >= 1000 and price < 2000 ):
    print (price - (price * 10 / 100))
elif(price >= 2000):
    print (price - (price * 15 / 100))
    