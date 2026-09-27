import tkinter as tk
from tkinter import messagebox

# List of characters
list_of_letters = ['`', 'u', '0', '}', '_', '<', 'E', 'S', 't', "'", '|', 'G', '~', '%', '$', '(', 'B', 'F', 'L', 'T', 'n', 
                   'l', 'b', '^', 'C', '¬', 'z', 'J', 'p', '1', 'N', 'A', '£', '=', 'x', '9', 'd', 'W', '7', '4', 'Q', '"', 
                   'w', '3', '{', 'y', ':', 'g', 'o', '2', '.', '6', '-', 'v', 'K', ',', 'j', 'c', '!', '>', '?', 'R', 
                   'k', ' ', 'q', 'f', 's', ';', 'i', ')', 'O', 'V', 'Y', 'M', '/', 'a', 'X', 'h', ']', 'D', 'e', '*', 
                   '&', 'U', '@', 'H', 'I', '[', '+', '8', 'Z', 'P', 'r', '5', 'm', '#']

# Functions
def caesar_cipher_encrypt(input_str, key):
    output = ""
    for i in range(len(input_str)):
        try:
            index = (list_of_letters.index(input_str[i]) - int(key[i % len(key)])) % len(list_of_letters)
            output += list_of_letters[index]
        except ValueError:
            messagebox.showerror("Error", "Invalid character in input.")
            return ""
    return output

def caesar_cipher_decrypt(input_str, key):
    output = ""
    for i in range(len(input_str)):
        try:
            index = (list_of_letters.index(input_str[i]) + int(key[i % len(key)])) % len(list_of_letters)
            output += list_of_letters[index]
        except ValueError:
            messagebox.showerror("Error", "Invalid character in input.")
            return ""
    return output

def process_text():
    mode = mode_var.get()
    text = input_text.get()
    key = key_entry.get()

    if not key.isdigit():
        messagebox.showerror("Error", "Key must contain only digits.")
        return

    key_list = [int(digit) for digit in key]  # Convert key into a list of integers
    if mode == "Encrypt":
        result = caesar_cipher_encrypt(text, key_list)
    elif mode == "Decrypt":
        result = caesar_cipher_decrypt(text, key_list)
    else:
        messagebox.showerror("Error", "Invalid mode selected.")
        return

    output_text.set(result)

def copy_to_clipboard():
    output = output_text.get()
    if output:
        root.clipboard_clear()
        root.clipboard_append(output)
        root.update()  # Keep clipboard updated
        messagebox.showinfo("Success", "Output copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No output to copy.")

# GUI
root = tk.Tk()
root.title("Encryption Program")
root.geometry("425x225")

# Input Text
tk.Label(root, text="Input Text:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
input_text = tk.StringVar()
tk.Entry(root, textvariable=input_text, width=50).grid(row=0, column=1, padx=10, pady=10)

# Key
tk.Label(root, text="Key:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
key_entry = tk.Entry(root, width=20)
key_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Mode
tk.Label(root, text="Mode:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
mode_var = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt").grid(row=2, column=1, padx=100, sticky="w")

# Output
tk.Label(root, text="Output Text:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
output_text = tk.StringVar()
output_entry = tk.Entry(root, textvariable=output_text, width=50, state="readonly")
output_entry.grid(row=3, column=1, padx=10, pady=10)

# Buttons
tk.Button(root, text="Process", command=process_text).grid(row=4, column=0, pady=20)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=4, column=1, pady=20, sticky="e")

#Makes sure GUI cant be resized
root.resizable(False, False)

root.mainloop()
