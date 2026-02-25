import re

def log_action(action_function):
    def wrapper(*args, **kwargs):
        print(f"\nStarting {action_function.__name__} process...")
        return action_function(*args, **kwargs)
    return wrapper

def validate_phone(phone):
    return re.match(r"^[0-9]{10}$", phone)

def vaidate(password):
    return len(password) >= 8
    