inventory = {
    "GPU workstation": (4, "good")
}

def add_item(inventory, name, quantity, condition="good"):
    inventory[name]=(quantity,condition)

def update_quantity(inventory,name,new_quantity):
    if name in inventory:
        old_condition = inventory[name][1]
        # tuple can't be updated, so creaed a new tuple
        inventory[name] = (new_quantity,old_condition)
    else:
        print("Item not found")

def delete_item(inventory,name):
    if name in inventory:
        del inventory[name]
    else:
        print("Item not found")

def search_item(inventory, name):
    if name in inventory:
        print(name, ":", inventory[name])
    else:
        print("Item not found")

def list_everything(inventory):
    print("Inventory:", inventory)
    conditions = set()
    for item in inventory:
        conditions.add(inventory[item][1])
    print("Conditions set:", conditions)

while True:
    print("\n1. Add Item\n2. Update quantity\ndelete \nSearch \nList everything\nexit")
    
    choice = input("enter choice: ")
    
    if choice == "1":
        name = input("Enter name: ")
        quantity = int(input("Enter quantity: "))
        condition = input("Enter condition: ")
        if condition == "":
            add_item(inventory, name, quantity)
        else:
            add_item(inventory, name, quantity, condition)           
    elif choice == "2":
        name = input("Enter name: ")
        quantity = int(input("Enter new quantity: "))
        update_quantity(inventory, name, quantity)       
    elif choice == "3":
        name = input("Enter name: ")
        delete_item(inventory, name)       
    elif choice == "4":
        name = input("Enter name: ")
        search_item(inventory, name)       
    elif choice == "5":
        list_everything(inventory)       
    elif choice == "6":
        break      