import json
import os
from hashlib import sha256

class AuthSystem:
    def __init__(self, db_file='users.json'):
        self.db_file = db_file
        self.users = self._load_users()

    def _load_users(self):
        if not os.path.exists(self.db_file):
            return {}
        with open(self.db_file, 'r') as f:
            return json.load(f)

    def _save_users(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.users, f, indent=4)

    def _hash_password(self, password):
        """Creates a secure hash of the password."""
        return sha256(password.encode()).hexdigest()

    def register(self, username, password, role='staff'):
        """Registers a new user (admin or staff)."""
        if username in self.users:
            return False, "Username already exists."
        
        self.users[username] = {
            "password": self._hash_password(password),
            "role": role
        }
        self._save_users()
        return True, f"User {username} registered as {role}."

    def login(self, username, password):
        """Authenticates the user and returns their role."""
        user = self.users.get(username)
        if user and user['password'] == self._hash_password(password):
            return True, user['role']
        return False, None

# --- Example Usage ---
if __name__ == "__main__":
    auth = AuthSystem()
    
    # 1. Register an Admin (one-time setup)
    # auth.register("manager_joe", "coffee123", role="admin")
    
    # 2. Login Flow
    print("--- Coffee Shop Login ---")
    user = input("Username: ")
    pw = input("Password: ")
    
    success, role = auth.login(user, pw)
    
    if success:
        print(f"Welcome back, {user}! Access Level: {role.upper()}")
        if role == 'admin':
            print("Redirecting to Inventory Management...")
        else:
            print("Redirecting to POS/Order Screen...")
    else:
        print("Login failed. Please check your credentials.")