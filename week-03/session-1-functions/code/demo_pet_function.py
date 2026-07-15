"""
Demo: Pet Function (Live-Coded Example from Class)
Shows: combining default params, *args, **kwargs in one function
This is the EXACT pattern you need for Project 3's calculate_total()
"""

def describe_pet(name, species="dog", *tricks, **extra_info):
    """
    Describe a pet with flexible details.

    Args:
        name: Pet's name (required)
        species: Type of animal (default: "dog")
        *tricks: Any number of tricks the pet knows
        **extra_info: Additional details (age, color, weight, etc.)

    Returns:
        None (prints description)
    """
    print(f"\n{name} is a {species}")

    if tricks:
        print(f"Tricks: {', '.join(tricks)}")

    if extra_info:
        print("Details:")
        for key, value in extra_info.items():
            print(f"  {key}: {value}")

# Example 1: Just name (uses default species)
describe_pet("Buddy")
# Buddy is a dog

# Example 2: Name and species
describe_pet("Whiskers", "cat")
# Whiskers is a cat

# Example 3: Name, species, and tricks
describe_pet("Max", "dog", "sit", "fetch", "roll over")
# Max is a dog
# Tricks: sit, fetch, roll over

# Example 4: Everything
describe_pet("Whiskers", "cat", "jump", "hide", age=3, color="orange", weight="8 lbs")
# Whiskers is a cat
# Tricks: jump, hide
# Details:
#   age: 3
#   color: orange
#   weight: 8 lbs

print("\n--- Mapping to Cart Engine ---")
print("In Project 3, you'll have a similar signature:")
print("def calculate_total(cart_items, discount_coupon=None, **fees):")
print("  - cart_items is required (like name)")
print("  - discount_coupon has a default (like species)")
print("  - **fees accepts arbitrary fees: tax=0.08, shipping=5.99, handling=2.00")
