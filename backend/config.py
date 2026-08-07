import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', '')

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("No DATABASE_URL set for Flask application. Please configure it in your environment variables.")
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
