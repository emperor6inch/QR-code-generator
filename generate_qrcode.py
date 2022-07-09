import generate_qrcode

input_URL = "https://www.google.com/"

qr = qrcode.QRCode(
    version = 1,
    error_connection = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png ")

print(qr.data_list)