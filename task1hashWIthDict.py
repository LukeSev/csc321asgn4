import hashlib
import time
import random
import string
import csv
from Crypto.Random import get_random_bytes


def hash_string(str):
    # Returns str hashed using sha256
    return hashlib.sha256(str.encode())

def hash_and_truncate(m, size):
    # Truncate hashed string to first 8 bytes
    h = int(hashlib.sha256(m.encode()).hexdigest(),16)
    return bin(h)[len(bin(h))-size:]
    # h = hashlib.sha256(m.encode())
    # h = h.hexdigest()
    # h = h[len(h)-(size//8):]
    # print(h)
    # return str(h)
def collision_stats(m0, size):
    # Given a message and the size of hash in bits, repeatedly generate and hash numbers til a collision is reached
    # Then output stats on how long it took and how many total inputs were generated
    hashDict = {}
    start = time.time()
    # h0 = hash_and_truncate(m0, size)
    # m1 = ''.join(random.choices(string.ascii_lowercase, k=8)) # Generate 8-char string
    # h1 = hash_and_truncate(m1, size)
    inputs = 1
    while(1):
        m1 = ''.join(random.choices(string.ascii_lowercase, k=8)) # Generate new string
        h1 = hash_and_truncate(m1, size)
        # print(h1)
        if(hashDict.get(h1) != None and hashDict.get(h1) != m1):
            break
        hashDict.update({h1:m1})
        inputs += 1
    end = time.time()
    print("Collision found!")
    print("Input message: " + m0)
    # print("Input hash bin: " + h0)
    print("Colliding message: " + m1)
    print("Colliding hash bin: " + h1)
    print("Input Size: " + str(size))
    print("Number of Inputs: " + str(inputs))
    print("Time to get Collision: " + str(end-start) + " seconds\n") # Extra newline for readability
    # Return collision stats as array for writing
    return [str(size), str(inputs), str(end-start)]

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

    header = ["Digest Size", "Inputs Generated", "Collision Time"]
    with open('dataTest.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    # Gather collision stats for every even-length size from 8 to 50
        for size in range(8, 52, 2):
            m = ''.join(random.choices(string.ascii_lowercase, k=8))
            writer.writerow(collision_stats(m, size))

if __name__ == '__main__':
    main()
