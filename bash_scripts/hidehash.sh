#!/bin/bash

# Function to hash and obfuscate user's password input
hidehash () { 
    HASH=$(echo $passvar | sha256sum | awk '{print $1}')
    echo -e "Password has been hashed..."; sleep 1
} 

# Function to encrypt and obfuscate user's password input
encryptpass () { 
    STRING="$passvar"
    SALT=$(/usr/bin/openssl rand -hex 8)
    K=$(/usr/bin/openssl rand -hex 12)
    ENCRYPTED=$(echo "$STRING" | /usr/bin/openssl enc -aes256 -a -A -S "${SALT}" -k "${K}")
    echo $ENCRYPTED > decryptmelater.txt
    echo $SALT >> decryptmelater.txt
    echo $K >> decryptmelater.txt
    sleep 2
    echo -e "Generating encryption key and salts...\nPassword has been encrypted..."; sleep 1
} 

# Function to decrypt a user's password
#decryptpass () {
## Usage: decryptpass <encrypted password> <salt value> <encryption key>
#read "Enter encrypted password string: " decryptme #Store encrypted password
#read "Enter salt value: " saltkey                  #Store salt value
#read "Enter encryption key string: " encryptkey    #Store encryption key
#echo $decryptme | /usr/bin/openssl enc -aes256 -d -a -A -S $saltkey -k $encryptkey
#sleep 1
#}

read -sp "Enter password: " passvar; echo -e "\n" # Capture user's password entry

hidehash # Call to hashing function
echo -e "Cleartext password: $passvar"  # Print password input in cleartext
echo -e "Hashed password: $HASH\n"      # Print password input as a hash

encryptpass # Call to encryption function

# Print user's password input in ciphertext
echo -e "Encrypted password: ${ENCRYPTED}\n\tEncryption Key: ${K}\n\tSalts: ${SALT}\n"
