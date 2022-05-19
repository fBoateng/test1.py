'''itemsAndPrice = {'Coke': 6, 'Sprite': 6, 'Malt': 8, 'Alvaro': 10}
for item in itemsAndPrice:
    new = itemsAndPrice.popitem()
    new1 = new.value()
    total = sum(new1)
print(total)'''

'''items = ['milk', 'sugar','sprite','water']
qnty = [10, 15, 5, 10]
price = [8, 2, 7, 4]


print('Items available are milk, sugar, sprite and water.')
user = input('Please enter the item you want? ')
userqnty = int(input('Please enter the quantity of items you want? '))

if user == items[0]:
    x = qnty[0]
    itemsold= x - userqnty
    print(f'You bought {userqnty} {items[0]}')
    y = userqnty * price[0]
    print(f'Pay {y} cedis')
    print(f'{itemsold} {items[0]} left')
    tp = (price[0] * itemsold) + (price[1] * itemsold) + (price[2] * itemsold) + (price[3] * itemsold)
    print(f'the prices of items left is {tp} cedis')

elif user == items[1]:
    x = qnty[1]
    itemsold= x - userqnty
    print(f'You bought {userqnty} {items[1]}')
    y = userqnty * price[1]
    print(f'Pay {y} cedis')
    print(f'{itemsold} {items[1]}left')
    tp = (price[0] * itemsold) + (price[1] * itemsold) + (price[2] * itemsold) + (price[3] * itemsold)
    print(f'the prices of items left is {tp} cedis')
    print(tp)
elif user == items[2]:
    x = qnty[2]
    itemsold= x - userqnty
    print(f'You bought {userqnty} {items[2]}')
    tp = (price[0] * itemsold) + (price[1] * itemsold) + (price[2] * itemsold) + (price[3] * itemsold)
    print(f'the prices of items left is {tp} cedis')
    y = userqnty * price[2]
    print(f'Pay {y} cedis')
    print(f'{itemsold} {items[2]}left')
    tp = (price[0] * itemsold) + (price[1] * itemsold) + (price[2] * itemsold) + (price[3] * itemsold)
    print(f'the prices of items left is {tp} cedis')
elif user == items[3]:
    x = qnty[3]
    itemsold= x - userqnty
    print(f'You bought {userqnty} {items[3]}')
    y = userqnty * price[3]
    print(f'Pay {y} cedis')
    print(f'{itemsold} {items[3]}left')
    tp = (price[0] * itemsold) + (price[1] * itemsold) + (price[2] * itemsold) + (price[3] * itemsold)
    print(f'the prices of items left is {tp} cedis')'''

u = []
q = []
p = []
userItems = input('Please enter the name of item? ')
Itemqnty = int(input('Please enter the quantity of items? '))
itemPrice = float(input('Please enter the price of the item? '))

userItems1 = input('Please enter the name of item? ')
Itemqnty1 = int(input('Please enter the quantity of items? '))
itemPrice1 = float(input('Please enter the price of the item? '))

userItems2 = input('Please enter the name of item? ')
Itemqnty2 = int(input('Please enter the quantity of items? '))
itemPrice2 = float(input('Please enter the price of the item? '))

userItems3 = input('Please enter the name of item? ')
Itemqnty3 = int(input('Please enter the quantity of items? '))
itemPrice3 = float(input('Please enter the price of the item? '))

u.append(userItems)
q.append(Itemqnty)
p.append(itemPrice)

u.append(userItems1)
q.append(Itemqnty1)
p.append(itemPrice1)

u.append(userItems2)
q.append(Itemqnty2)
p.append(itemPrice2)

u.append(userItems3)
q.append(Itemqnty3)
p.append(itemPrice3)

user = input('Please enter the item you want? ')
userqnty = int(input('Please enter the quantity of items you want? '))

for item in u:
    if user == item:
        print(f'You bought {userqnty}, {user}')

for qnty in q:
    if user == item:
        qntyLeft = qnty - userqnty
print(f'You sold {userqnty} {user}, you have {qntyLeft} left')
for pce in p:
    totalPrice = pce*qnty
    print(totalPrice)
    priceLeft = pce * qntyLeft
print(f'Prices of items left is {priceLeft} ')

totalQnty = qnty-userqnty
print(f'{qnty}-{userqnty} = {totalQnty}')

if totalQnty == 0:
    userItems = input('Please enter the name of item? ')










