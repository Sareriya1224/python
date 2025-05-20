
# Restaurant Ordering System

# Menu Dictionary
menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'coffee': 80,
    'salad': 70
}

# Welcome Message
print("🍽️ Welcome to Python Restaurant!")
print("📋 Here's our menu:")
for item, price in menu.items():
    print(f" - {item.capitalize()}: ₹{price}")

# Initialize order and total
order_list = []
order_total = 0

while True:
    item = input("\nEnter the item you'd like to order: ").lower()
    
    if item in menu:
        order_total += menu[item]
        order_list.append(item)
        print(f"{item.capitalize()} added to your order.")
    else:
        print("❌ Sorry, that item is not on the menu.")

    # Ask if they want to add another item
    another = input("Would you like to order something else? (yes/no): ").lower()
    if another != 'yes':
        break

# Final Summary
print("\n🧾 Order Summary:")
for i, item in enumerate(order_list, 1):
    print(f"{i}. {item.capitalize()} - ₹{menu[item]}")
print(f"\n💰 Total Bill: ₹{order_total}")
print("🙏 Thank you for ordering from Python Restaurant!")
