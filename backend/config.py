import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-me')

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///instance/devconnect.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Frontend Configuration
    FRONTEND_URL = os.environ.get('FRONTEND_URL', 'http://localhost:5173')

    # Admin Configuration
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', '')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', '')

    # Session Security
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_PERMANENT = False
