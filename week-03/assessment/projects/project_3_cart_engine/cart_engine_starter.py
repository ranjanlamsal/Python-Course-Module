"""
Project 3: E-Commerce Cart Engine
Starter file—implement the TODOs below.
"""

# TODO 1: Implement add_item function
def add_item(cart, name, price, quantity=1):
    """
    Add an item to the cart.

    Args:
        cart: List of item dicts
        name: Item name (str)
        price: Item price (float)
        quantity: Item quantity (int, default 1)
    """
    pass  # Your code here


# TODO 2: Implement remove_item function
def remove_item(cart, name):
    """
    Remove an item from cart by name (case-insensitive).

    Args:
        cart: List of item dicts
        name: Item name to remove

    Returns:
        bool: True if removed, False if not found
    """
    pass  # Your code here


# TODO 3: Implement display_cart function
def display_cart(cart):
    """
    Display cart contents formatted.

    Args:
        cart: List of item dicts
    """
    if not cart:
        print("Cart is empty")
        return

    print(f"Cart ({len(cart)} items):")
    # Your code here to display each item
    # Format: "  Laptop: $1000.00 x 1 = $1000.00"

    subtotal = calculate_subtotal(cart)
    print(f"Subtotal: ${subtotal:.2f}")


# TODO 4: Implement calculate_subtotal function
def calculate_subtotal(cart):
    """
    Calculate sum of price * quantity for all items.

    Args:
        cart: List of item dicts

    Returns:
        float: Subtotal
    """
    pass  # Your code here


# TODO 5: Implement calculate_total function
def calculate_total(cart, discount_coupon=None, **fees):
    """
    Calculate final total with discount and fees.

    Args:
        cart: List of item dicts
        discount_coupon: Optional dict {"code": "...", "percent": ..., "min_purchase": ...}
        **fees: Arbitrary fees (tax=0.08, shipping=10, handling=2, etc.)

    Returns:
        dict: Breakdown {"subtotal": ..., "discount": ..., "fees": ..., "total": ...}
    """
    subtotal = calculate_subtotal(cart)

    # Apply discount if provided and minimum purchase met
    discount = 0
    if discount_coupon:
        # Your code here
        pass

    # Sum all fees
    total_fees = sum(fees.values())

    final_total = subtotal - discount + total_fees

    return {
        "subtotal": subtotal,
        "discount": discount,
        "discount_code": discount_coupon["code"] if discount_coupon else None,
        "fees": fees,
        "total": final_total
    }


# TODO 6: Implement sort and filter helpers using lambda
def sort_cart_by_price(cart, reverse=False):
    """Sort cart by price using lambda."""
    pass  # Your code here


def sort_cart_by_name(cart):
    """Sort cart by name (alphabetical) using lambda."""
    pass  # Your code here


def filter_expensive_items(cart, min_price):
    """Filter items with price >= min_price using lambda."""
    pass  # Your code here


# TODO 7: Implement main loop
def main():
    """Main command loop."""
    cart = []
    print("Welcome to Cart Engine!")
    print("\nCommands:")
    print("  add <name> <price> [quantity]")
    print("  remove <name>")
    print("  show")
    print("  checkout")
    print("  quit")

    while True:
        command = input("\n> ").strip().split()

        if not command:
            continue

        action = command[0].lower()

        # TODO: Implement command handling
        # if action == "add" and len(command) >= 3:
        #     ...
        # elif action == "remove" and len(command) >= 2:
        #     ...
        # elif action == "show":
        #     ...
        # elif action == "checkout":
        #     ...
        # elif action == "quit":
        #     ...
        # else:
        #     print("Invalid command")

        pass  # Your code here


if __name__ == "__main__":
    main()
