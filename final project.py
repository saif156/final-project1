#Commando Restaurant
#Menu list

menu={
    "Pizza": 1250,
    "Burger": 250,
    "Salad": 70,
    "Chicken roll": 150,
    "Tea": 100,
    "Coffee": 150,
    "Fries": 100,
    "Cold drink 2.5 ltr": 350
}

#Greeting
print("Welcome to Commando Restaurant")
print("Pizza: Rs1250\n Burger: Rs250\n Salad: Rs70\n Chicken roll: Rs150\n Tea: Rs100\n Coffee: Rs150\n Fries: Rs100\n Cold drink 2.5 ltr: Rs350")

order_total=1250
order_total=250
order_total=70

#1250+150=1400

item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total+=menu[item_1] #0+1250
    print(f"your item{item_1} has been added to your order")
else:
    print(f"Ordered item{item_1} is available yet!")

print(f"The total amount of item to pay is {order_total}")