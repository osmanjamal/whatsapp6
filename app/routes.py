from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app.models import db, MenuItem, Order, Customer
from app.whatsapp.message_processor import process_whatsapp_message

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/menu')
def menu():
    menu_items = MenuItem.query.all()
    return render_template('menu.html', menu_items=menu_items)

@main.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        customer_phone = request.form['phone']
        items = request.form.getlist('items')
        
        customer = Customer.query.filter_by(phone=customer_phone).first()
        if not customer:
            customer = Customer(phone=customer_phone)
            db.session.add(customer)
        
        new_order = Order(customer=customer, status='new')
        for item_id in items:
            menu_item = MenuItem.query.get(item_id)
            new_order.items.append(menu_item)
        
        db.session.add(new_order)
        db.session.commit()
        
        return redirect(url_for('main.order_status', order_id=new_order.id))
    
    menu_items = MenuItem.query.all()
    return render_template('order.html', menu_items=menu_items)

@main.route('/status/<int:order_id>')
def order_status(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('order_status.html', order=order)

@main.route('/whatsapp/webhook', methods=['POST'])
def whatsapp_webhook():
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

@main.route('/whatsapp/webhook', methods=['GET'])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == "YOUR_VERIFY_TOKEN":
            return challenge, 200
        else:
            return "Forbidden", 403
    return "Bad Request", 400