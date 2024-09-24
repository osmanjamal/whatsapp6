from app.models import db, Customer, Order, MenuItem

def process_whatsapp_message(sender, message):
    customer = Customer.query.filter_by(phone=sender).first()
    if not customer:
        customer = Customer(phone=sender)
        db.session.add(customer)
        db.session.commit()
    
    if message.lower() == 'menu':
        return get_menu()
    elif message.lower().startswith('order'):
        return process_order(customer, message)
    else:
        return "مرحباً بك في مطعم المحاشي! يمكنك طلب القائمة بإرسال كلمة 'menu' أو تقديم طلب بإرسال 'order' متبوعًا بأرقام الأصناف."

def get_menu():
    menu_items = MenuItem.query.all()
    menu_text = "قائمة المحاشي:\n"
    for item in menu_items:
        menu_text += f"{item.id}. {item.name} - {item.price} درهم\n"
    return menu_text

def process_order(customer, message):
    order_items = message.split()[1:]
    if not order_items:
        return "الرجاء تحديد أرقام الأصناف التي تريد طلبها."
    
    new_order = Order(customer=customer, status='new')
    db.session.add(new_order)
    
    order_summary = "طلبك:\n"
    for item_id in order_items:
        menu_item = MenuItem.query.get(int(item_id))
        if menu_item:
            new_order.items.append(menu_item)
            order_summary += f"- {menu_item.name}\n"
    
    db.session.commit()
    
    return f"{order_summary}\nرقم طلبك هو: {new_order.id}. شكرًا لطلبك من مطعم المحاشي!"