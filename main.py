from tkinter import*
import qrcode

from tkinter import messagebox
from PIL import Image, ImageTk

# Function to generate QR code
def generate_qr():
    data = entry.get()
    if data.strip() == "":
        messagebox.showerror("Error", "Please enter some text or link")
        return
    
    # Generate QR
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save("qrcode.png")
    
    # Show image in Tkinter window
    qr_img = Image.open("qrcode.png")
    qr_img = qr_img.resize((200, 200))  # Resize for display
    tk_img = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=tk_img)
    qr_label.image = tk_img
    
    messagebox.showinfo("Success", "QR Code Generated and Saved as qrcode.png")

# GUI Setup
root = Tk()
root.title("QR Code Generator")
root.geometry("400x450")
root.config(bg="white")

title = Label(root, text="QR Code Generator", font=("Arial", 18, "bold"), bg="white")
title.pack(pady=10)

entry = Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

btn = Button(root, text="Generate QR Code", command=generate_qr, font=("Arial", 12), bg="green", fg="white")
btn.pack(pady=10)

qr_label = Label(root, bg="white")
qr_label.pack(pady=20)

root.mainloop()

