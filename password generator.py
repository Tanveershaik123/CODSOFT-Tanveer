import tkinter as tk
import random
import string

def generate_password(length, include_spl_char):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation if include_spl_char else ''
    all_char = lower + upper + digits + special
    
    if include_spl_char:
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(special)
        ]
        password += random.choices(all_char, k=length - 4)
    else:
        password = random.choices(all_char, k=length)
    
    random.shuffle(password)
    return ''.join(password)

def on_generate():
    try:
        length = int(entry_length.get())
        include_special_chars = var_special_chars.get()
        password = generate_password(length, include_special_chars)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        entry_password.delete(0, tk.END)
        entry_password.insert(0, "Invalid length")

root = tk.Tk()
root.title("Password Generator")

# Labels and entry widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=5)

# Checkbox for special characters
var_special_chars = tk.BooleanVar()
chk_special_chars = tk.Checkbutton(root, text="Include Special Characters", variable=var_special_chars)
chk_special_chars.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Generate button
btn_generate = tk.Button(root, text="Generate Password", command=on_generate)
btn_generate.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Label and entry for displaying the password
tk.Label(root, text="Generated Password:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(root, width=50)
entry_password.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()
