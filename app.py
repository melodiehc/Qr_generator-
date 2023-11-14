 
import qrcode
img = qrcode.make('https://outlook.office.com/mail/sentitems')
type(img)  # qrcode.image.pil.PilImage
img.save("QR_code.png") #qr image file name 

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")