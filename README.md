# نظام إدارة مطعم المحاشي عبر WhatsApp

هذا النظام يدير طلبات مطعم المحاشي عبر WhatsApp ويوفر لوحة تحكم للإدارة.

## المتطلبات

- Python 3.7+
- Flask
- SQLAlchemy
- WhatsApp Business API

## التثبيت

1. قم بنسخ المستودع:
   ```
   git clone [رابط المستودع]
   ```

2. قم بإنشاء بيئة افتراضية وتفعيلها:
   ```
   python -m venv venv
   source venv/bin/activate  # على Linux/Mac
   venv\Scripts\activate  # على Windows
   ```

3. قم بتثبيت المتطلبات:
   ```
   pip install -r requirements.txt
   ```

4. قم بإنشاء ملف `.env` وتعبئة المتغيرات البيئية اللازمة.

5. قم بتشغيل التطبيق:
   ```
   flask run
   ```

## الاستخدام

- يمكن للعملاء التفاعل مع النظام عبر WhatsApp.
- يمكن للإدارة الوصول إلى لوحة التحكم عبر `/admin`.

## المساهمة

نرحب بالمساهمات! يرجى فتح issue أو تقديم pull request.

## الترخيص

[MIT License](https://opensource.org/licenses/MIT)