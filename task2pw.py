import bcrypt
from nltk.corpus import words
import base64
import time

def crack_pw(salt, hash, words):
    # Given a salt, its hash, and a list of words,
    # Find which word from the list hashes to same value
    for w in words:
        # Only test hash word if its within char limit for password
        if (len(w) > 5) and (len(w) < 11):
            pwhash = bcrypt.hashpw(w.encode(), salt.encode())
            if pwhash == (salt+hash).encode():
                return w
    # If password never found, return default msg
    return "PASSWORD NOT FOUND"

def main():
    # Read and process each line and crack its password
    # wordlist = nltk.corpus.words.words()
    with open("shadow.txt", "r") as file:
        for line in file: # Keep going while there's a line in file
            i = 0
            while line[i] != '$':
                i += 1
            user = line[:i]
            salt = line[i:i+29]
            hash = line[i+29:-1]

            print("\nUSER: " + user[:-1] + "\nSALT: " + salt + "\nHASH: " + hash)
            # print("SALT LENGTH: " + str(len(salt)) + "\nHASH LENGTH: " + str(len(hash)) + "\n")

            start = time.time()
            pw = crack_pw(salt, hash, words.words())
            end = time.time()
            print(user[:-1] + "'s password cracked after " + str(end - start) + "seconds")
            print("Password: " + pw + "\n") 

if __name__ == '__main__':
    main()
