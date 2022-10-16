
import bcrypt
import nltk.corpus
import time

def crack_pw(salt, hash, words):

    # Given a salt, its hash, and a list of words,
    # Find which word from the list hashes to same value
    for w in words:
        # Only test hash word if its within char limit for password
        if((len(w) >= 6) and (len(w) <= 10)):
            pwhash = bcrypt.hashpw(w.encode("latin1"), salt.encode("latin1"))
            if(pwhash.decode("latin1") == hash):
                return w
    # If password never found, return default msg
    return "PASSWORD NOT FOUND"


def main():
    # Read and process each line and crack its password
    nltk_words = nltk.corpus.words.words()
    with open("shadow.txt", "r") as file:
        for line in file: # Keep going while there's a line in file
            i = 0
            while line[i] != '$':
                i += 1
            user = line[:i]
            salt = line[i:i+29]
            hash = line[i+29:]

            print("\nUSER: " + user + "\nSALT: " + salt + "\nHASH: " + salt+hash + "\n")

            start = time.time()
            pw = crack_pw(salt, salt+hash, nltk_words)
            end = time.time()
            print(user[:-1] + "'s password cracked after " + str(end - start) + "seconds")
            print("Password: " + pw + "\n") 

if __name__ == '__main__':
    main()
