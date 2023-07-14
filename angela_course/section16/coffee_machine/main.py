from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine = MoneyMachine()
maker = CoffeeMaker()
m = Menu()

go_on = True
while go_on:
    choice = input(f"What would you like? ({m.get_items()}): ").lower()
    if choice == "report": 
        maker.report()
        machine.report()
    elif choice == "off":
        go_on = False
    else:
        menu_item = m.find_drink(choice)
        if menu_item == None: 
            continue
        if maker.is_resource_sufficient(menu_item):
            if machine.make_payment(menu_item.cost):
                maker.make_coffee(menu_item)