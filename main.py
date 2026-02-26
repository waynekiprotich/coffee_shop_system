from auth import Auth
from order import Order
from storage import Storage
from utils import log_action
#menu
coffee_menu = {
    "1": {"name": "Espresso", "price": 200},
    "2": {"name": "Latte", "price": 250},
    "3": {"name": "Cappuccino", "price": 300}
}
#size
coffee_size = {
    "small": 1,
    "medium": 1.2,
    "large": 1.5
}
# loading orders from storage
def load_orders():
    return Storage.load("orders.json")
# save orders to storage
def save_orders(order):
    
    orders = load_orders()
    
    if not isinstance(orders , dict):
        orders = {}
    orders[order.order_id] = order.to_dict()
    
    Storage.save("orders.json", orders)
    
# Handles coffee ordering
@log_action # decorator from utils
def place_order(phone):
    print(f"coffee_menu")
    
    for key , value in coffee_menu.items():
      print(f"{key}. {value['name']} - KSH {value['price']}")
      
    choice = input("Select Coffee :")
    
    if choice not in coffee_menu:
        print("INVALID CHOICE")
        return
    
    size = input("Choose size :")
    if size not in coffee_size:
        print("INVALID SIZE")
        return
    
    coffee = coffee_menu[choice]
    price = coffee['price'] * coffee_size[size]
    
    order_id = str(len(load_orders()) +1 ) 
    order = Order(
        order_id,
        phone,
        coffee["name"],
        size,
        price
    )
    
    save_orders(order)
    print("Order placed successfully")
# viewing orders as admin    
def view_orders():
    orders =load_orders()
    if not orders:
        print(f"No orders found")
        return
    
    for order in orders.values():
        print(f"""
                Order ID: {order.get('order_id')}
                Phone: {order.get('phone')}
                Coffee: {order.get('coffee')}
                Size: {order.get('size')}
                Price: KSH {order.get('price')}
                -------------------
                """)
# calculating the total revenue as admin       
def view_total_revenue():
    orders = load_orders()
    
    total = 0
    for order in orders.values():
        total += float(order["price"])
    print(f"Your total revenue is {total}")
    
def customer_menu(phone):
    while True:
        print("\nCustomer Menu")
        print("1. Place Order")
        print("2. Logout")

        choice = input("> ")

        if choice == "1":
            place_order(phone)

        else:
            break
# load admin menu
def admin_menu():
    while True:
        print("\nAdmin Dashboard")
        print("1. View Orders")
        print("2. Total Revenue")
        print("3. Logout")

        choice = input("Enter :")

        if choice == "1":
            view_orders()

        elif choice == "2":
            view_total_revenue()

        else:
            break
#load main menu       
def main_menu():
    while True:

        print("\nRiverside Coffee System")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("> ")

        if choice == "1":

            phone = input("Phone: ")
            password = input("Password: ")

            role = Auth.login(phone, password)

            if role:
                print("Login successful")

                if role == "customer":
                    customer_menu(phone)

                elif role == "admin":
                    admin_menu()

            else:
                print("Login failed")

        elif choice == "2":

            username = input("Username: ")
            phone = input("Phone: ")
            password = input("Password: ")

            Auth.register(username, phone, password)

        else:
            break