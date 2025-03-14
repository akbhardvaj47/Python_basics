import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=5, border=2)
qr.add_data("www.linkedin.com/in/amit-kr-bhardvaj-81176b309")
qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="white")
img.save("ak_Profile.png")