from flask import Blueprint, jsonify
from app.models import MenuItem, Order

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "مرحبًا بك في نظام إدارة مطعم المحاشي!"

@main.route('/menu')
def get_menu():
    menu_items = MenuItem.query.all()
    return jsonify([{"id": item.id, "name": item.name, "price": item.price} for item in menu_items])

@main.route('/orders')
def get_orders():
    orders = Order.query.all()
    return jsonify([{"id": order.id, "status": order.status, "total_price": order.total_price} for order in orders])