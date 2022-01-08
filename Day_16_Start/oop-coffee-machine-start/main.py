
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
monney_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
# menu_item=MenuItem()
menu=Menu()

is_no=True

while is_no:
    option=menu.get_items()
    choice=input(f"what you would to like {option} : ")
    if choice=="report":
        coffee_maker.report()
        monney_machine.report()
    elif choice=="off":
        is_no=False
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if monney_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


