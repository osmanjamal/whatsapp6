import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///restaurant.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WHATSAPP_API_TOKEN = os.environ.get('WHATSAPP_API_TOKEN')
    WHATSAPP_PHONE_NUMBER_ID = os.environ.get('WHATSAPP_PHONE_NUMBER_ID')
    WHATSAPP_BUSINESS_ACCOUNT_ID = os.environ.get('WHATSAPP_BUSINESS_ACCOUNT_ID')
    WHATSAPP_RECIPIENT_PHONE_NUMBER = os.environ.get('WHATSAPP_RECIPIENT_PHONE_NUMBER')
    WHATSAPP_VERIFY_TOKEN = os.environ.get('WHATSAPP_VERIFY_TOKEN')