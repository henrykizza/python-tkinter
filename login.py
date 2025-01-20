 
import tkinter as tk
from tkinter import messagebox

# Predefined username and password
valid_username = "user123"
valid_password = "password123"

def check_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == valid_username and password == valid_password:
        messagebox.showinfo("Login Successful", "You have logged in successfully!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Create and place the username label and entry widget
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Create and place the password label and entry widget
label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")  # Password field (hidden text)
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Create and place the submit button
button_submit = tk.Button(root, text="Submit", command=check_login)
button_submit.grid(row=2, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
