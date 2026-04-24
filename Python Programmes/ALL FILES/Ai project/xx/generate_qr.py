import qrcode

data = "http://10.226.186.137:5000"

qr = qrcode.make(data)
qr.save("robot_qr.png")

print("QR generated successfully!")
