
from hashlib import sha256

class hash_class():
    def hash_password(self,password):
        return sha256(password.encode()).hexdigest()