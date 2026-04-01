import qrcode
import os

link = input("Enter your URL: ")

img = qrcode.make(link)
img.save("qrcode.png")

print("✅ QR Code saved!")

# Open automatically
os.startfile("qrcode.png")