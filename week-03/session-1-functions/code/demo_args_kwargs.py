"""
Demo: *args and **kwargs
Shows: arbitrary positional and keyword arguments
"""

def sum_all(*numbers):
    """Sum an arbitrary number of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))           # 6
print(sum_all(10, 20, 30, 40, 50)) # 150
print(sum_all())                  # 0 (empty tuple)

def print_info(name, **details):
    """Print a person's name and arbitrary details."""
    print(f"\n{name}'s Info:")
    for key, value in details.items():
        print(f"  {key}: {value}")

print_info("Alice", age=30, city="NYC", job="Engineer")
print_info("Bob", age=25, country="USA")

def make_profile(username, *hobbies, **settings):
    """
    Create a user profile with hobbies and settings.

    Args:
        username: User's name (required)
        *hobbies: Any number of hobbies
        **settings: Additional settings (theme, language, etc.)
    """
    profile = {"username": username}

    if hobbies:
        profile["hobbies"] = list(hobbies)

    profile["settings"] = settings
    return profile

profile1 = make_profile("alice", "reading", "coding", theme="dark", language="en")
print(f"\nProfile: {profile1}")
# Profile: {'username': 'alice', 'hobbies': ['reading', 'coding'], 'settings': {'theme': 'dark', 'language': 'en'}}
