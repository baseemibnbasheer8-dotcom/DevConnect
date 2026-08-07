import os
from functools import wraps
from flask import Flask, request, session, redirect, url_for, render_template, flash
from flask_cors import CORS
from config import Config
from models import db, Message
from routes import api_bp
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

def create_app(config_class=Config):
    load_dotenv(override=True)
    app = Flask(__name__)
    app.config.from_object(config_class)


    # Allow CORS only for the frontend origin
    frontend_url = app.config.get('FRONTEND_URL', '*')
    CORS(app, resources={r"/api/*": {"origins": frontend_url}})

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(api_bp)

    # Create tables
    with app.app_context():
        db.create_all()

    # Authentication decorator
    def login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not session.get('admin_logged_in'):
                return redirect(url_for('admin_login'))
            return f(*args, **kwargs)
        return decorated_function

    # Cache Control Header to prevent browser caching of admin pages
    @app.after_request
    def add_cache_control(response):
        if request.path.startswith('/admin'):
            response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
        return response

    # Admin Routes
    @app.route('/admin')
    @app.route('/admin/')
    def admin_root():
        return redirect(url_for('admin_dashboard'))

    @app.route('/admin/login', methods=['GET', 'POST'])
    def admin_login():
        if session.get('admin_logged_in'):
            return redirect(url_for('admin_dashboard'))

        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            admin_username = app.config.get('ADMIN_USERNAME')
            admin_password = app.config.get('ADMIN_PASSWORD')

            if (
                username == admin_username
                and password == admin_password
            ):
                session['admin_logged_in'] = True
                flash('Login successful.', 'success')
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Invalid username or password.', 'error')
                return render_template('admin/login.html')

        return render_template('admin/login.html')

    @app.route('/admin/dashboard', methods=['GET'])
    @login_required
    def admin_dashboard():
        messages = Message.query.order_by(Message.created_at.desc()).all()
        return render_template('admin/dashboard.html', messages=messages)

    @app.route('/admin/messages/<int:id>/delete', methods=['POST'])
    @login_required
    def delete_message(id):
        msg = Message.query.get(id)
        if msg:
            db.session.delete(msg)
            db.session.commit()
            flash('Message deleted successfully.', 'success')
        else:
            flash('Message not found.', 'error')
        return redirect(url_for('admin_dashboard'))

    @app.route('/admin/logout', methods=['POST'])
    @login_required
    def admin_logout():
        session.clear()
        flash('Logged out successfully.', 'success')
        return redirect(url_for('admin_login'))

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
