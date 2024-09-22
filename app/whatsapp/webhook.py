from flask import Blueprint, request, jsonify
from app.whatsapp.message_processor import process_whatsapp_message
from config import Config

whatsapp = Blueprint('whatsapp', __name__)

@whatsapp.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if 'entry' in data and data['entry']:
        changes = data['entry'][0].get('changes', [])
        if changes and 'value' in changes[0]:
            value = changes[0]['value']
            if 'messages' in value and value['messages']:
                message = value['messages'][0]
                sender = message['from']
                text = message['text']['body']
                response = process_whatsapp_message(sender, text)
                # Here you would typically send the response back to WhatsApp
                print(f"Response to {sender}: {response}")
    return jsonify({"status": "success"}), 200

@whatsapp.route('/webhook', methods=['GET'])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == Config.WHATSAPP_VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Forbidden", 403
    return "Bad Request", 400