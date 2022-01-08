

# def Process_coins(quarter, dimes, nickeles, pennies):
#     """ get coins and return money in dollar """
#     total= quarter*0.25+dimes * 0.10 + nickeles * 0.05+pennies * 0.01
#     return round(total)
# def check_money(insert_money,choice):
#     """ check user insert money is sufficient or not """
#     if insert_money>=MENU[choice]["cost"]:
#         change=insert_money-MENU[choice]["cost"]
#         return change
#     elif insert_money<MENU[choice]["cost"]:
#         return "Sorry that's not enough money. Money refunded."
# def check_resources(resouces,choice):
#     if resouces["water"]<MENU[choice]["ingredients"]["water"]:
#         return "Sorry there is not enough water."
#     elif resouces["milk"]<MENU[choice]["ingredients"]["milk"]:
#         return "Sorry there is not enough milk."
#     elif resouces["coffee"]<MENU[choice]["ingredients"]["coffee"]:
#         return "Sorry there is not enough coffee."


# choice=input("What would you like? (espresso/latte/cappuccino):")
# # print(MENU[choice]["cost"])
# print("Please insert coins.")
# quarter=float(input( "how many quarters?:"))
# dimes=float(input("how many dimes?: ")) 
# nickeles=float(input("how many nickles?:"))   
# pennies=float(input("how many pennies?:"))
# insert_money=Process_coins(quarter, dimes, nickeles, pennies)

# money=check_money(insert_money,choice)
# # print(MENU[choice]["ingredients"]["water"])
# resoure=check_resources(resources,choice)




MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
} 
profit=0

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
      if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item} .")
            return False
    return True
def Process_coins():
    print("Please insert coins.")
    total=int(input("How many quarters?"))*0.25
    total+=int(input("How many dimes?"))*0.10
    total+=int(input("How many nickles?"))*0.05
    total+=int(input("How many pennies?"))*0.01
    return total
def  is_transaction_successful(insert_money,coffee_cost):
    if coffee_cost<=insert_money:
        change=round( insert_money-coffee_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def Make_Coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}☕️. Enjoy!")
    
is_on=True
while is_on:
    choice= input("What would you like? (espresso/latte/cappuccino):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print (f"Milk: {resources['milk']}ml")
        print (f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment= Process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                Make_Coffee(choice,drink["ingredients"])



