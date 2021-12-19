# IMPORT THIS FILES IF YOU DON`T HAVE THIS INSTALL IT BY USING "pip install qrcode" BY TYPING IN CMD
import qrcode
import image

# THE SIZE OF THE QR-CODE BOX
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5,
)

# PASTE ANY LINK OF WHICH YOU WANT TO MAKE QR-CODE OR TYPE THE MESSAGE YOU WANT TO TELL ANYONE THROUGH QR-CODE
data = "https://www.instagram.com/het08"

# THE DATA WILL BE STORE HERE AND THE IMAGIE WILL BE CREATED OF QR-CODE FROM THIS CODE
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("qr.png")
