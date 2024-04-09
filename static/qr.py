import qrcode

# Generate the QR code
data = "https://127.0.0.1:5000/feedback"
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")
