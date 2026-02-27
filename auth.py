import json
import os
from hashlib import sha256
import storage
from utils import validate_phone, validate_password


class Auth:

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
