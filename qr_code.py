import qrcode

# Data to be encoded in the QR code
data = "https://www.youtube.com/@codeXudaya"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    # controls the error correction used for the QR Code
    box_size=10,  
    # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes to use for the border
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode_image.png")