from werkzeug.security import generate_password_hash, check_password_hash

# Mock database (In a real app, this would be SQLAlchemy or MongoDB)
users_db = {}

def register_user(username, password):
    """Hashes the password and saves the user."""
    if username in users_db:
        return False, "User already exists!"
    
    # We use pbkdf2:sha256 by default for security
    hashed_password = generate_password_hash(password)
    users_db[username] = hashed_password
    return True, "User registered successfully!"

def login_user(username, password):
    """Checks the provided password against the stored hash."""
    hashed_password = users_db.get(username)
    
    if not hashed_password:
        return False, "User not found!"
    
    # check_password_hash handles the salt and comparison
    if check_password_hash(hashed_password, password):
        return True, "Login successful!"
    else:
        return False, "Invalid password!"

# --- Quick Test ---
if __name__ == "__main__":
    # Registering
    register_user("tech_enthusiast", "SuperSecret123")
    
    # Login Attempt
    success, message = login_user("tech_enthusiast", "SuperSecret123")
    print(f"Status: {success}, Message: {message}")