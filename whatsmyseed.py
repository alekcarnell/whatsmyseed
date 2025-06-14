# A program that brute-forces a 12 word seed phrase and compares it
# to the hash of the 12 words in the correct order. 
#
# The idea is that you might distribute your seed via "Shamirs Secret" and 
# then also provide this program so that all parties can confirm the order
# of the words they were given. 

# Imports
import hashlib
from itertools import permutations

# Declare Variable
wordlist = []
targetHash = "b09110cd01e9b93074d215c37c4ceabe1f54620238ed1efcb5d920b3ffd092ec"

# test = hashlib.sha256(str(testlist).encode()).hexdigest()
# print(test)

print("Please enter the 12 words you were given in any order. Please enter them individually without any capitals or spaces.")

# Get wordlist from user
for i in range(12):
    word = input(f"Enter word {i + 1}: ").strip()
    wordlist.append(word)

# Function that will hash whatever is fed to it and compare it to our target hash
def hash_seed(phrase: str) -> str:
    return hashlib.sha256(phrase.encode()).hexdigest()

# Brute force all permutations
for i, perm in enumerate(permutations(wordlist)):
    seed_phrase = " ".join(perm)
    hashed = hash_seed(seed_phrase)

    if hashed == targetHash:
        print("Found it! Your seed phrase is: ", seed_phrase)
        break

    if i % 100000 == 0:
        print(f"Checked {i} permutations...")



