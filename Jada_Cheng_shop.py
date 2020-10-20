#shop.py

print("Greetings, Customer!")
items = input("How many items would you like to buy? ")
print("Milk = $2.61")
print("Toothpaste = $2.27")
print("Chips = $2.65")
print("Cookies = $2.85")
print("Floss = $3.46")

price = input("Your total cost is...")
print(2.61+2.27+2.65+2.85+3.46)

payment = input("How would you like to pay? Cash or Card? ")

def check_money(total_cost, customer_money):
    if customer_money > total_cost:
        print("Can pay")
    elif customer_money < total_cost:
        print("Can't pay")
    else:
        print("Invaild input")

#This should print False
can_pay = check_money(13.84, 12)


#This should print True
can_pay = check_money(13.84, 14)


print("Thank you, have a nice day!")


#I added what I did in lab Activity problem 4 but i'm really sure of this how you wanted.
