from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Order, MenuItem
from app import db

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    return render_template('admin/index.html')

@admin.route('/orders')
def orders():
    orders = Order.query.all()
    return render_template('admin/orders.html', orders=orders)

@admin.route('/menu')
def menu():
    menu_items = MenuItem.query.all()
    return render_template('admin/menu.html', menu_items=menu_items)

@admin.route('/add_menu_item', methods=['GET', 'POST'])
def add_menu_item():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        description = request.form['description']
        new_item = MenuItem(name=name, price=price, description=description)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('admin.menu'))
    return render_template('admin/add_menu_item.html')