from main import MENU, resources


def Process_coins(quarter, dimes, nickeles, pennies):
    total = quarter*0.25+dimes * 0.10 + nickeles * 0.05+pennies * 0.01

    return total


print("What would you like? (espresso/latte/cappuccino):")
print("Please insert coins.")
quarter=int(input( "how many quarters?:"))
dimes=int(input("how many dimes?: ")) 
nickeles=int(input("how many nickles?:"))   
pennies=int(input("how many pennies?:"))     
print(Process_coins(quarter, dimes, nickeles, pennies))