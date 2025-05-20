
# Restaurant Management System

# Sample menu with stock and prices
menu = {
    'pizza': {'price': 40, 'stock': 10},
    'pasta': {'price': 50, 'stock': 10},
    'burger': {'price': 60, 'stock': 10},
    'coffee': {'price': 80, 'stock': 10},
    'salad': {'price': 70, 'stock': 10}
}

# Order history
orders = []

def display_menu():
    print("\n📋 Current Menu:")
    for item, details in menu.items():
        print(f"{item.capitalize()} - ₹{details['price']} (Stock: {details['stock']})")

def take_order():
    order = {}
    total = 0
    while True:
        display_menu()
        item = input("\nEnter item name to order (or 'done' to finish): ").lower()
        if item == 'done':
            break
        if item in menu and menu[item]['stock'] > 0:
            quantity = int(input(f"Enter quantity of {item}: "))
            if quantity <= menu[item]['stock']:
                cost = menu[item]['price'] * quantity
                total += cost
                order[item] = quantity
                menu[item]['stock'] -= quantity
                print(f"{quantity} x {item.capitalize()} added to order. Subtotal: ₹{cost}")
            else:
                print(f"Only {menu[item]['stock']} left in stock.")
        else:
            print("❌ Item not available or out of stock.")
    orders.append({'items': order, 'total': total})
    print(f"✅ Order placed! Total amount: ₹{total}")

def view_orders():
    print("\n📦 All Orders:")
    if not orders:
        print("No orders placed yet.")
        return
    for idx, order in enumerate(orders, 1):
        print(f"\nOrder {idx}:")
        for item, qty in order['items'].items():
            print(f" - {item.capitalize()}: {qty} pcs")
        print(f"Total: ₹{order['total']}")

def restock_item():
    item = input("Enter item to restock: ").lower()
    if item in menu:
        qty = int(input("Enter quantity to add: "))
        menu[item]['stock'] += qty
        print(f"{item.capitalize()} restocked by {qty}. New stock: {menu[item]['stock']}")
    else:
        print("Item not found in menu.")

def main():
    while True:
        print("\n=== Restaurant Management System ===")
        print("1. Display Menu")
        print("2. Take Order")
        print("3. View Orders")
        print("4. Restock Item")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            display_menu()
        elif choice == '2':
            take_order()
        elif choice == '3':
            view_orders()
        elif choice == '4':
            restock_item()
        elif choice == '5':
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
