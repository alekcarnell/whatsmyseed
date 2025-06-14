# Summary
whatsmyseed is a fairly straightfoward program that initializes a hash of a known 12-word BIP39 seed phrase and then takes in 12 words as input and brute forces all arrangements of those words against the known hash. Once it finds the correct order, it reads it back to the user. 

# Purpose
The idea is that someone might distribute their seed phrase via "Shamirs Secret" - where they give multiple parties just parts of the seed phrase - And then those parties could come together to put in their words into this program to find the corect order. 

# Goal
To have a way to still fully self-custody a 12-word seed phrase but have a way for trusted heirs/inheritors to obtain the seed
