import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Requires Pillow library

# Install Pillow first: pip install pillow

# Hardcoded valid credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "s3cr3t_p@ss"

def check_credentials():
    username = entry_username.get()
    password = entry_password.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Success", "Login successful! Flag: CTF{Tk1nt3r_R3v3rs3d}")
    else:
        messagebox.showerror("Error", "Invalid credentials!")

# Create main window
root = tk.Tk()
root.title("Secure login")
root.geometry("800x600")

# Set window icon
try:
    root.iconbitmap('icon.ico')
except Exception as e:
    print("Icon error:", e)

# Load and set background image
try:
    bg_image = Image.open("background.jpg")
    bg_photo = ImageTk.PhotoImage(bg_image.resize((800, 600)))
    background_label = tk.Label(root, image=bg_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print("Background image error:", e)
    bg_photo = None

# Create main container
main_frame = tk.Frame(root, bg='white', bd=2, relief=tk.RIDGE)
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Styled input container
input_frame = tk.Frame(main_frame, bg='white', padx=20, pady=20)
input_frame.pack(padx=10, pady=10)

# Custom styled widgets
style = ttk.Style()
style.configure('TEntry', padding=5, relief='flat')

# Username field
username_frame = tk.Frame(input_frame, bg='#e0e0e0', bd=1, relief=tk.SOLID)
username_frame.pack(pady=10, fill=tk.X)

label_username = tk.Label(username_frame, text="Username:", bg='#e0e0e0', fg='#333333')
label_username.pack(side=tk.LEFT, padx=5)

entry_username = ttk.Entry(username_frame, style='TEntry')
entry_username.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=5)

# Password field
password_frame = tk.Frame(input_frame, bg='#e0e0e0', bd=1, relief=tk.SOLID)
password_frame.pack(pady=10, fill=tk.X)

label_password = tk.Label(password_frame, text="Password:", bg='#e0e0e0', fg='#333333')
label_password.pack(side=tk.LEFT, padx=5)

entry_password = ttk.Entry(password_frame, show="*", style='TEntry')
entry_password.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=5)

# Login button
btn_login = tk.Button(input_frame, text="Login", command=check_credentials,
                     bg='#4CAF50', fg='white', activebackground='#45a049',
                     relief=tk.FLAT, padx=20, pady=5)
btn_login.pack(pady=20)

# Keep reference to the image
root.bg_photo = bg_photo  # Prevent garbage collection

root.mainloop()
