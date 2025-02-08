import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def open_box():
    box_button.pack_forget()
    img_label.pack(pady=10)
    message_label.pack()
    propose_button.pack(pady=10)

def propose():
    messagebox.showinfo("Proposal", "Will You Marry Me? 💍")

root = tk.Tk()
root.title("Propose Day")
root.geometry("400x500")
root.configure(bg="pink")

box_button = tk.Button(root, text="Open The Box 🎁", font=("Arial", 14), bg="red", fg="white", command=lambda: (box_button.pack(), open_box()))
box_button.pack(pady=50)

<img id="photo" src="your-photo.jpg.jpeg" alt="Our Photo">
image = image.resize((150, 150), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
img_label = tk.Label(root, image=photo)

message_label = tk.Label(root, text="My Love ❤️\nFrom the moment we met, my heart knew you were the one.\nWill you be mine forever?", font=("Arial", 12), bg="white", wraplength=300, justify="center")

propose_button = tk.Button(root, text="Will You Marry Me? 💍", font=("Arial", 14), bg="red", fg="white", command=propose)

root.mainloop()
