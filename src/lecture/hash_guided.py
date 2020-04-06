"""
What is an hash function and how does it work?

- Deterministic: for a given input, the output will always be the same
- Definied output range: For a hash table of size 16, all keys must hash to a value 0-15. For smaller, values, this is usually accomplished using the modulo % operation.
- Predictable Speed: Hash functions for has tables should be lightning fast while cryptographic hashes (like bcrypt) should be very slow.
- Non-invertible: You should not be able to reconstruct the input value from the output. This trait is imporant in cryptographic hashes but not necessary for general hash tables.

"""

import time
import hashlib
import bcrypt

n = 1000000
key = b"STR"

print(f"Hashing {n}x")

start_time = time.time()
for i in range(n):
    hash(key)
end_time = time.time()
print (f"  Python hash runtime: {end_time - start_time} seconds")


start_time = time.time()
for i in range(n):
    hashlib.sha256(key)
end_time = time.time()
print (f"  SHA256 hash runtime: {end_time - start_time} seconds")


def djb2(key):
    # Start from an arbitrary large prime
    hash_value = 5381
    # Bit-shift and sum value for each character
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
    return hash_value
    
start_time = time.time()
for i in range(n):
    djb2(key)
end_time = time.time()
print (f"  DJB2 hash runtime: {end_time - start_time} seconds")


n=10
print(f"\nHashing {n}x")
salt = bcrypt.gensalt()
start_time = time.time()
for i in range(n):
    bcrypt.hashpw(b"KEY",salt)
end_time = time.time()
print (f"  bcrypt hash runtime: {end_time - start_time} seconds")


"""
What is a hash table and how does it work?

- Hash Tables have an underlying Array structure
- This is why they are fast at accessing elements as arrays
- The main difference is that Hash Tables are indexed using a hash function in an unordered fashion, whereas arrays are indexed via continguous ordered indices

"""

# self.storage = [None, None, <"Key", "value">, None, None, None, None, None]
import math 

arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

def smallest_sum(arr):
    count = 0
    for i in arr:
        value = min(i)
        count += value
    return count

print(smallest_sum(arr))