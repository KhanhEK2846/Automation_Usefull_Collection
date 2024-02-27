import qrcode,os, pathlib

dirPath = pathlib.Path(__file__).parent.absolute()
outPath = str(dirPath) + ".\output\\"
dirs =os.listdir(outPath)

data = input("Data to QR code: ")

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=5,)

def QR():
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(outPath+'QR.png')

QR()