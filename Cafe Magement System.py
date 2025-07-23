import configparser
import os

class Cafe:
    def __init__(self):
        self.menu = self.load_menu()
        self.orders = []

    def load_menu(self):
        # Debug output to help diagnose issues
        print(f"🔍 Current working directory: {os.getcwd()}")
        print(f"📂 Files found: {os.listdir()}")

        config = configparser.ConfigParser()
        config.read("menu.txt")

        if not config.sections():
            print("⚠️  menu.txt found but is empty or formatted incorrectly!")
            return {}

        menu = {}
        for category in config.sections():
            items = {}
            for item, price in config.items(category):
                items[item.strip().lower()] = int(price)
            menu[category] = items
        return menu

    def show_menu(self):
        if not self.menu:
            print("❌ No menu items to display.")
            return

        print("\n------ MENU ------")
        for category, items in self.menu.items():
            print(f"\n[{category}]")
            for item, price in items.items():
                print(f"{item.title()} - ₹{price}")
        print("------------------")

    def take_order(self):
        self.show_menu()
        if not self.menu:
            print("⚠️  Cannot take orders — menu is empty!")
            return

        print("\nType 'done' to finish ordering.")
        while True:
            item = input("Enter item name: ").strip().lower()
            if item == "done":
                break
            found = False
            for items in self.menu.values():
                if item in items:
                    qty = input(f"Enter quantity of {item.title()}: ")
                    if qty.isdigit():
                        self.orders.append((item.title(), int(qty), items[item]))
                        print(f"✅ Added {qty} x {item.title()} to order.")
                    else:
                        print("❌ Quantity must be a number.")
                    found = True
                    break
            if not found:
                print("❌ Item not found in menu.")

    def show_bill(self):
        if not self.orders:
            print("🧾 No items ordered.")
            return

        print("\n----- BILL -----")
        total = 0
        for item, qty, price in self.orders:
            amount = qty * price
            print(f"{item} x {qty} = ₹{amount}")
            total += amount
        print(f"Total Amount: ₹{total}")
        print("----------------")

    def start(self):
        while True:
            print("\n--- Cafe Management ---")
            print("1. Take Order")
            print("2. Show Bill")
            print("3. Exit")
            choice = input("Choose option: ")
            if choice == "1":
                self.take_order()
            elif choice == "2":
                self.show_bill()
            elif choice == "3":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice.")

if __name__ == "__main__":
    cafe = Cafe()
    cafe.start()