from app import db
from datetime import datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    orders = db.relationship('Order', backref='customer', lazy=True)

    def __repr__(self):
        return f'<Customer {self.phone}>'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='new')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_price = db.Column(db.Float, default=0.0)
    items = db.relationship('OrderItem', back_populates='order')

    def __repr__(self):
        return f'<Order {self.id}>'

    def calculate_total_price(self):
        self.total_price = sum(item.menu_item.price * item.quantity for item in self.items)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    is_available = db.Column(db.Boolean, default=True)
    order_items = db.relationship('OrderItem', back_populates='menu_item')

    def __repr__(self):
        return f'<MenuItem {self.name}>'

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    order = db.relationship('Order', back_populates='items')
    menu_item = db.relationship('MenuItem', back_populates='order_items')

    def __repr__(self):
        return f'<OrderItem {self.id}>'

def init_db():
    db.create_all()
    
    # إضافة بعض عناصر القائمة الافتراضية
    if MenuItem.query.count() == 0:
        default_items = [
            MenuItem(name='محشي ورق عنب', price=15.0, description='ورق عنب محشي بالأرز والتوابل', is_available=True),
            MenuItem(name='محشي كوسا', price=18.0, description='كوسا محشية باللحم المفروم والأرز', is_available=True),
            MenuItem(name='محشي باذنجان', price=16.0, description='باذنجان محشي بالخضار والأرز', is_available=True),
            MenuItem(name='محشي ملفوف', price=17.0, description='ملفوف محشي باللحم والأرز', is_available=True)
        ]
        db.session.add_all(default_items)
        db.session.commit()
    
    print("تم تهيئة قاعدة البيانات وإضافة العناصر الافتراضية.")

# يمكنك استدعاء هذه الدالة في ملف app/__init__.py