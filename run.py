from app import create_app, db
from app.models import Customer, Order, MenuItem, OrderItem

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Customer': Customer, 'Order': Order, 'MenuItem': MenuItem, 'OrderItem': OrderItem}

if __name__ == '__main__':
    app.run()