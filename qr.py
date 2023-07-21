import qrcode

imagine = qrcode.make("https://127.0.0.1.8000")

imagine.save("qr.png")