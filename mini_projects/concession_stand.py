concession_stand = {"popcorn":1.00
                    ,"hotdog":2.00
                    ,"soda":1.00}
cart = []
total =0
print("|----MENU----|")
for key,value in concession_stand.items():
    
    print(f"{key:5}:{value}")
    print("------------")
while True:
    food = input("select an item (q to quit)").lower()
    if food =="q":
        break
    elif concession_stand.get(food) is not None :
        cart.append(food)
for food in cart:
    total+=concession_stand.get(food)
    print(food,end=" ")
    print()
print("------------")
print(f"Total is ${total}")
print("------------")
