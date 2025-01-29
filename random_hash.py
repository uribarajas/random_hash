import hashlib
import random
import string

def generate_random_string(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def find_hash():
    for _ in range(1000):
        random_string = generate_random_string()
        hash_value = hashlib.sha256(random_string.encode()).hexdigest()
        
        if hash_value.startswith("00"):
            print(f"Hash encontrado: {hash_value}")
            return True
    
    print("No se encontró un hash con dos ceros consecutivos al inicio.")
    return False

if __name__ == "__main__":
    find_hash()
