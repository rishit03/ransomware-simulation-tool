import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

# Generate and save encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("ransom_key.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Key Generated", "Encryption key saved as 'ransom_key.key'. Keep it safe!")

# Load encryption key
def load_key():
    if not os.path.exists("ransom_key.key"):
        messagebox.showerror("Error", "Key file not found! Generate a new key first.")
        return None
    return open("ransom_key.key", "rb").read()

# Encrypt files
def encrypt_files():
    directory = filedialog.askdirectory(title="Select Folder to Encrypt")
    if not directory:
        return

    key = load_key()
    if key is None:
        return

    cipher = Fernet(key)

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file != "ransom_key.key":
            with open(file_path, "rb") as f:
                file_data = f.read()
            encrypted_data = cipher.encrypt(file_data)
            with open(file_path, "wb") as f:
                f.write(encrypted_data)

    messagebox.showinfo("Encryption Complete", "All files in the folder have been encrypted!")

# Decrypt files
def decrypt_files():
    directory = filedialog.askdirectory(title="Select Folder to Decrypt")
    if not directory:
        return

    key = load_key()
    if key is None:
        return

    cipher = Fernet(key)

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file != "ransom_key.key":
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            decrypted_data = cipher.decrypt(encrypted_data)
            with open(file_path, "wb") as f:
                f.write(decrypted_data)

    messagebox.showinfo("Decryption Complete", "All files in the folder have been decrypted!")

# GUI Setup
root = tk.Tk()
root.title("🔐 Ransomware Simulation & Recovery Tool")
root.geometry("400x300")

label = tk.Label(root, text="Ransomware Simulation Tool", font=("Arial", 14, "bold"))
label.pack(pady=10)

btn_generate_key = tk.Button(root, text="Generate Encryption Key", command=generate_key, bg="blue", fg="black", width=30)
btn_generate_key.pack(pady=5)

btn_encrypt = tk.Button(root, text="Encrypt Files", command=encrypt_files, bg="red", fg="black", width=30)
btn_encrypt.pack(pady=5)

btn_decrypt = tk.Button(root, text="Decrypt Files", command=decrypt_files, bg="green", fg="black", width=30)
btn_decrypt.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", command=root.quit, bg="gray", fg="black", width=30)
btn_exit.pack(pady=20)

root.mainloop()
