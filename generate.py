import qrcode

data = "https://example.com"
img = qrcode.make(data)
img.save("qrcode.png")

print("QR code generated")
