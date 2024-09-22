import unittest
from app import create_app, db
from app.models import Customer, Order, MenuItem

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('مرحبًا بك في نظام إدارة مطعم المحاشي', response.data.decode())

    def test_menu_api(self):
        with self.app.app_context():
            menu_item = MenuItem(name='محشي ورق عنب', price=15.0, description='لذيذ جداً')
            db.session.add(menu_item)
            db.session.commit()

        response = self.client.get('/menu')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'محشي ورق عنب')

if __name__ == '__main__':
    unittest.main()