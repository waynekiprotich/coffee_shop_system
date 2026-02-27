import json     #Used for working with JSON data (though not directly used here)
import os        #Operating systems related to functions
from hashlib import sha256    
import storage    #Custom module for handling data storage and retrieval
from utils import validate_phone, validate_password

      #Authentication class 
class Auth:

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

#register new users
    def register(self, username, phone, password, role="customer"):

        if not validate_phone(phone):
            print("Invalid phone number")
            return False

        if not validate_password(password):
            print("Password must be at least 8 characters")
            return False

        users = Storage.load("users.json")

        if phone in users:
            print("User already exists")
            return False

        users[phone] = {
            "username": username,
            "password": self.hash_password(password),
            "role": role
        }

        Storage.save("users.json", users)

        print("Registration successful")
        return True


    def login(self, phone, password):

        users = Storage.load("users.json")

        hashed = self.hash_password(password)

        if phone in users and users[phone]["password"] == hashed:
            return users[phone]["role"]

        return None