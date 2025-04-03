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

def print_report(resources,pro):
    print(f"""
     Machine Report:
    💧 Water: {resources["water"]} ml
    🥛 Milk: {resources["milk"]} ml
    ☕ Coffee: {resources["coffee"]} g
    💰 Profit: ${pro}
    """)

def checking_resources(we_want,total):
    """Checking that all resources are present or not"""
    for i in we_want["ingredients"]:
        if we_want["ingredients"][f"{i}"]>total[f"{i}"]:
            print(f"🔻Sorry there is no enough🔻 {i}")
            return False
    return True

def process_coins(cost,selected,resources):
    """quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01"""
    print("💰 Please insert coins:")
    total=0
    total += int(input("🔻Number of quarters: "))*0.25
    total += int(input("🔻Number of dimes: "))*0.10
    total += int(input("🔻Number of nickles: "))*0.05
    total += int(input("🔻Number of pennies: "))*0.01

    global profit   #Triggering Global to change profit which is not in function
    if total>=cost:
        change=(total-cost)
        print(f"Here is ${change:.2f} in change!Collect it")
        print("🔄 Preparing Your Order... ☕")
        profit+=cost
        for i in selected["ingredients"]:
            resources[i]-=selected["ingredients"][i]
        return 1
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0

def make_coffee(user_choice):
    print(f"Here is your {user_choice}☕️. Enjoy!😊.")

profit=0
flag=True
while flag:
    choice=input("What would you like? (espresso/latte/cappuccino)").lower().strip()
    if choice=="off":
        print("Turning off the machine😊")
        flag=False
    elif choice=="report":
        print_report(resources,profit)
    elif choice in MENU:
        selected=MENU[f"{choice}"]  #selecting only the customer option
        if checking_resources(selected,resources):
            if process_coins(selected["cost"],selected,resources):
                make_coffee(choice)
    else:
        print("❌ Invalid choice. Please select espresso, latte, or cappuccino. ☕")
