from art import logo
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

def report(res):
    """Returns the report of remaining items in the resources"""
    for i in res:
        if i == "coffee":
            print(f"{i}: {res[i]}g")
        else:
            print(f"{i}: {res[i]}ml")

def res_deduction(res,menu,ans):
    """Deducts the resources based on the selected coffees ingredients"""
    for i in menu[ans]["ingredients"]:
        res[i] -= menu[ans]["ingredients"][i]

def res_sufficiency(res,menu,ans):
    """Checks if the selected ingredients are sufficient to make the order"""
    if ans not in menu: #incase the ans is (report or off) or the user had a typing error
        return False

    for i in menu[ans]["ingredients"]:
        if menu[ans]["ingredients"][i] > res[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def order(menu, res):
    on= True
    print(logo)
    
    while on:
        ans=input("What would you like? (espresso/latte/cappuccino): ").lower()

        if ans == "off":
            on= False

        elif ans == "report":
            report(res)

        elif res_sufficiency(res, menu, ans):
            print("Please insert coins.")
            total = float(input("how many quarters?: ")) * 0.25
            total += float(input("how many dimes?: ")) * 0.1
            total += float(input("how many nickles?: ")) * 0.05
            total += float(input("how many pennies?: ")) * 0.01

            if total < menu[f"{ans}"]["cost"]:
                print("insufficient funds")

            res_deduction(res,menu,ans)

            if total > menu[f"{ans}"]["cost"]:
                change= format(total - menu[f"{ans}"]["cost"], ".2f")
                print(f"Here is ${change} in change.")

            print("Here is your latte ☕️. Enjoy!")

order(MENU, resources)
