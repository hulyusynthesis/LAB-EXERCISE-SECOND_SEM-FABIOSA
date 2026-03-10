class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append(Item(name, price, quantity))
        print(f"\n'{name}' added to cart.")

    def remove_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"\n'{name}' removed from cart.")
                return
        print(f"\n'{name}' not found in cart.")

    def view_cart(self):
        if not self.items:
            print("\nYour cart is empty.")
            return
        print("\n--- Your Cart ---")
        for item in self.items:
            print(f"{item.name} x{item.quantity} = ${item.price * item.quantity:.2f}")
        print(f"Total: ${self.get_total():.2f}")

    def get_total(self):
        return sum(item.price * item.quantity for item in self.items)

    def checkout(self):
        if not self.items:
            print("\nYour cart is empty. Nothing to checkout.")
            return
        self.view_cart()
        print("\nCheckout successful! Thank you for shopping!")
        self.items.clear()


def main():
    cart = Cart()
    print("=== Shopping Cart Simulator ===")
    print("Commands: add, remove, view, checkout, quit")

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command == "add":
            name = input("Item name: ").strip()
            price = float(input("Price: $"))
            quantity = int(input("Quantity: "))
            cart.add_item(name, price, quantity)

        elif command == "remove":
            name = input("Item name to remove: ").strip()
            cart.remove_item(name)

        elif command == "view":
            cart.view_cart()

        elif command == "checkout":
            cart.checkout()

        elif command == "quit":
            print("\nGoodbye!")
            break

        else:
            print("\nUnknown command. Try: add, remove, view, checkout, quit")


if __name__ == "__main__":
    main()