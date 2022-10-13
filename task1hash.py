import hashlib
import time
from Crypto.Random import get_random_bytes

DIGEST_SIZE = 8

def hash_string(str):
    # Returns str hashed using sha256
    return hashlib.sha256(str.encode())

def hash_truncated(byts, size):
    # Truncate hashed string to firts 8 bytes
    return hashlib.sha256(byts).hexdigest()[:size]

def collision_stats(hexhash, size):
    # Given a hash and its size, repeatedly generate and hash numbers til a collision is reached
    # Then output stats on how long it took and how many total inputs were generated
    start = time.time()
    collider = hash_truncated(get_random_bytes(size), size)
    inputs = 1
    while(collider != hexhash):
        collider = hash_truncated(get_random_bytes(size), size)
        inputs += 1
    end = time.time()
    print("Collision found!")
    print("Input Size: " + str(size))
    print("Number of Inputs: " + str(inputs))
    print("Time to get Collision: " + str(end-start) + " seconds\n") # Extra newline for readability


def main():
    # Create 2 string with hamming distance 1
    str1 = "abcdefghij"
    str2 = "abcdefghik"
    hash1 = hash_string(str1)
    hash2 = hash_string(str2)
    # Print each string in binary form to confirm hamming distance
    print("String 1 bits: " + ' '.join(format(ord(x), 'b') for x in str1))
    print("String 2 bits: " + ' '.join(format(ord(x), 'b') for x in str2))
    # Print hex representation of the hash of each string
    print("Hash 1: " + hash1.hexdigest())    
    print("Hash 2: " + hash2.hexdigest())
    print() # Print newline for readability

    # Gather collision stats for every even-length size from 8 to 50
    for size in range(8, 50, 2):
        hexhash = hash_truncated(get_random_bytes(size), size)
        collision_stats(hexhash, size)

if __name__ == '__main__':
    main()
