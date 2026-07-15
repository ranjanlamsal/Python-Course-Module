# Project 3: E-Commerce Cart Engine

## Overview

Build a console-based shopping cart system that manages items, calculates totals with discounts and fees, and demonstrates flexible function signatures with `*args`, `**kwargs`, and lambda expressions.

**Estimated time:** 4-6 hours  
**Due:** Wednesday night

## Learning Objectives

- Write functions with default parameters, `*args`, and `**kwargs`
- Use lambda expressions with `filter()` and `sorted()`
- Organize code into reusable functions
- Test functions with different argument combinations

## Requirements

### Core Features (Required)

Your cart engine must support:

1. **Add items** to cart (name, price, quantity)
2. **Remove items** from cart by name
3. **Display cart** contents (formatted)
4. **Calculate subtotal** (sum of all item prices × quantities)
5. **Apply discount coupon** (percentage off, minimum purchase requirement)
6. **Apply fees** (tax, shipping, handling—flexible via `**kwargs`)
7. **Calculate final total** (subtotal - discount + fees)

### Technical Requirements

1. **Functions must demonstrate:**
   - Default parameters (e.g., `discount_percent=0`)
   - `**kwargs` for flexible fees
   - Lambda with `filter()` (e.g., filter items eligible for discount)
   - Lambda with `sorted()` (e.g., sort items by price or name)

2. **Function signatures (suggested, you can adjust):**
   ```python
   def add_item(cart, name, price, quantity=1)
   def remove_item(cart, name)
   def display_cart(cart)
   def calculate_subtotal(cart)
   def calculate_total(cart, discount_coupon=None, **fees)
   ```

3. **Data structure:**
   - Cart is a list of dicts: `[{"name": "...", "price": ..., "quantity": ...}, ...]`
   - Or use your own structure if you prefer

### Discount Rules

- Discount coupon format: `{"code": "SAVE10", "percent": 10, "min_purchase": 50}`
- Discount applies to **subtotal** (before fees)
- Only applies if subtotal ≥ `min_purchase`
- If minimum not met, ignore discount

### Example Interaction

```
Welcome to Cart Engine!

Commands:
  add <name> <price> [quantity]
  remove <name>
  show
  checkout
  quit

> add Laptop 1000
Added Laptop ($1000.00 x 1)

> add Mouse 25 2
Added Mouse ($25.00 x 2)

> show
Cart (3 items):
  Laptop: $1000.00 x 1 = $1000.00
  Mouse:  $25.00 x 2 = $50.00
Subtotal: $1050.00

> checkout
Enter discount code (or press Enter to skip): SAVE10
Subtotal: $1050.00
Discount (SAVE10 - 10%): -$105.00
Tax (8%): $75.60
Shipping: $10.00
Final Total: $1030.60

> quit
Goodbye!
```

## Implementation Guide

### Step 1: Data Structure

Define your cart structure:

```python
cart = [
    {"name": "Laptop", "price": 1000, "quantity": 1},
    {"name": "Mouse", "price": 25, "quantity": 2},
]
```

### Step 2: Basic Functions

Start with `add_item()`, `remove_item()`, `display_cart()`:

```python
def add_item(cart, name, price, quantity=1):
    """Add item to cart."""
    cart.append({"name": name, "price": price, "quantity": quantity})

def remove_item(cart, name):
    """Remove item by name (case-insensitive)."""
    # Use filter() or list comprehension
    pass

def display_cart(cart):
    """Display cart contents formatted."""
    pass
```

### Step 3: Calculations

Implement `calculate_subtotal()` and `calculate_total()`:

```python
def calculate_subtotal(cart):
    """Calculate sum of price * quantity for all items."""
    return sum(item["price"] * item["quantity"] for item in cart)

def calculate_total(cart, discount_coupon=None, **fees):
    """
    Calculate final total with discount and fees.

    Args:
        cart: List of cart items
        discount_coupon: Optional dict with discount rules
        **fees: Arbitrary fees (tax, shipping, handling, etc.)

    Returns:
        dict: Breakdown {"subtotal": ..., "discount": ..., "fees": ..., "total": ...}
    """
    subtotal = calculate_subtotal(cart)

    # Apply discount if provided and minimum met
    discount = 0
    if discount_coupon:
        # Your logic here
        pass

    # Sum all fees
    total_fees = sum(fees.values())

    final_total = subtotal - discount + total_fees

    return {
        "subtotal": subtotal,
        "discount": discount,
        "fees": fees,
        "total": final_total
    }
```

### Step 4: Lambda Expressions

Use lambda for filtering and sorting:

```python
# Filter expensive items (over $50)
expensive = list(filter(lambda item: item["price"] > 50, cart))

# Sort by price (descending)
sorted_by_price = sorted(cart, key=lambda item: item["price"], reverse=True)

# Sort by name (alphabetical)
sorted_by_name = sorted(cart, key=lambda item: item["name"].lower())
```

### Step 5: Main Loop

Create a command-line interface:

```python
def main():
    cart = []
    print("Welcome to Cart Engine!")

    while True:
        command = input("\n> ").strip().split()

        if not command:
            continue

        action = command[0].lower()

        if action == "add" and len(command) >= 3:
            name = command[1]
            price = float(command[2])
            quantity = int(command[3]) if len(command) > 3 else 1
            add_item(cart, name, price, quantity)
            print(f"Added {name}")

        elif action == "remove" and len(command) >= 2:
            name = command[1]
            remove_item(cart, name)
            print(f"Removed {name}")

        elif action == "show":
            display_cart(cart)

        elif action == "checkout":
            # Prompt for discount code, calculate total
            pass

        elif action == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
```

## Testing Checklist

Test these scenarios:

- [ ] Add items with and without quantity
- [ ] Remove item (case-insensitive)
- [ ] Display empty cart
- [ ] Display cart with multiple items
- [ ] Calculate subtotal correctly
- [ ] Apply discount when minimum is met
- [ ] Ignore discount when minimum is NOT met
- [ ] Apply multiple fees (tax, shipping, handling)
- [ ] Sort items by price and by name
- [ ] Filter items by price threshold

## Stretch Goals (Optional)

- Save cart to file (JSON format)
- Load cart from file
- Update item quantity (don't add duplicate, just increase quantity)
- Multiple discount codes (apply best one)
- Item categories (apply category-specific discounts)

## Submission

Submit `cart_engine_starter.py` (renamed to `cart_engine.py` with your implementation).

## Grading Criteria

- **Functionality (40%):** All core features work
- **Functions (30%):** Demonstrates default params, `**kwargs`, lambda
- **Code quality (20%):** Clear names, docstrings, organized
- **Testing (10%):** Edge cases handled (empty cart, invalid input)

## Common Mistakes

See [`../../common_mistakes.md`](../../common_mistakes.md) for patterns to avoid.

## Need Help?

- Re-read [`session-1-functions/`](../../../session-1-functions/)
- Run [`demo_pet_function.py`](../../../session-1-functions/code/demo_pet_function.py) — it has the exact `**kwargs` pattern you need
- Attend office hours
