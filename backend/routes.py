from flask import Blueprint, jsonify, request
from services import save_contact_message

api_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')

@api_bp.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "application": "DevConnect",
        "version": "1.0.0"
    }), 200

@api_bp.route('/about', methods=['GET'])
def about():
    return jsonify({
        "application": "DevConnect",
        "version": "1.0.0",
        "frontend": "React",
        "backend": "Flask"
    }), 200

@api_bp.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()

    if not data:
        return jsonify({"success": False, "message": "Invalid request"}), 400

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({
            "success": False, 
            "message": "Name, email, and message are required fields."
        }), 400

    success, error = save_contact_message(name, email, message)

    if success:
        return jsonify({
            "success": True,
            "message": "Message stored successfully"
        }), 201
    else:
        return jsonify({
            "success": False,
            "message": "Failed to store message. Please try again later."
        }), 500
