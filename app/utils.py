import requests
from config import Config

def send_whatsapp_message(to, message):
    url = f"https://graph.facebook.com/v12.0/{Config.WHATSAPP_PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {Config.WHATSAPP_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()