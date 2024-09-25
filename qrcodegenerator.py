import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr():
    link = entry.get()  
    if link:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save("qrcode.png")  

        img = Image.open("qrcode.png")
        img = img.resize((200, 200), Image.Resampling.LANCZOS)  
        img = ImageTk.PhotoImage(img)

        qr_code_label.config(image=img)
        qr_code_label.image = img

    else:
        messagebox.showerror("Error", "Please enter a link!")  # Show an error if no link is provided

root = Tk()
root.title("QR Code Generator")
root.geometry("400x400")

title_label = Label(root, text="Enter a link to generate QR Code", font=("Helvetica", 16))
title_label.pack(pady=20)

entry = Entry(root, width=50)
entry.pack(pady=10)

generate_button = Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

qr_code_label = Label(root)
qr_code_label.pack(pady=20)

root.mainloop()
