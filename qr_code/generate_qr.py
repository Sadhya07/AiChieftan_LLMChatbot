import qrcode

# Replace with your actual hosted URL
url = ""
img = qrcode.make(url)
img.save("hotel_chatbot_qr.png")
