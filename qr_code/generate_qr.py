import qrcode

# Replace with your actual hosted URL
url = "https://aichieftanllmchatbot-hospitality.streamlit.app"
img = qrcode.make(url)
img.save("hotel_chatbot_qr.png")
