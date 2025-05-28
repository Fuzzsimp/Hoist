import base64
import time

print("Welcome to HOIST")
#Loads input
sample_string = input("enter text ")
sample_string_bytes = sample_string.encode("ascii")

#Encrypts input
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
print("encoding into BASE64")
time.sleep(.6283185)
print(f"encoded string: {base64_string}") #Prints encryption

#De-encryptes for verification
decode_string_bytes = base64.b64decode(base64_bytes)
decode_string = decode_string_bytes.decode("ascii")

print(f"original string: {decode_string}")


#-----------------------------------------------

#loads cypher
def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

def decrypt_vigenere(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

#Brings in BASE64 string
text_to_encrypt = (f"{base64_string}")
#Brings in key
key = input("\n enter key: ")

print("encrypting...")
time.sleep(1.2)

#Prints outputs
encrypted_text = encrypt_vigenere(text_to_encrypt, key)
print(f"encrypted text: {encrypted_text}")

decrypted_text = decrypt_vigenere(encrypted_text, key)
print(f"original text: {decrypted_text}")
