import qrcode

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_L,
                   box_size = 10,
                   border = 2)

qr.add_data("https://www.vishnumano.com")
qr.make(fit = True)
img = qr.make_image(fill_color = "green", back_color = "black")
img.save("mycode.png")