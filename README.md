# DevConnect

DevConnect is a modern, clean, and responsive full-stack web application. It is built to be simple, beginner-friendly, and structured using industry best practices for future deployment using tools like Nginx, Systemd, and Ansible on Ubuntu Linux.

## Features
- **Frontend**: Built with React (Vite), React Router, Axios, and modern responsive CSS.
- **Backend**: Built with Python Flask, Blueprint for API versioning (`/api/v1`), Flask-CORS, SQLAlchemy, and SQLite.
- **Pages**: Home, About (fetching from API), and Contact (submitting data to the database).
- **Production Ready**: Uses environment variables, cleanly separated concerns, and centralized configurations.

## Technology Stack
- **Frontend**: React (Vite), Axios, React Router, CSS
- **Backend**: Python 3, Flask, SQLAlchemy, SQLite
- **Deployment-Ready**: Ready for Nginx, Systemd, and Ansible

## Folder Structure

```
DevConnect/
├── backend/                  # Flask REST API backend
│   ├── instance/             # SQLite database location (ignored in Git)
│   ├── app.py                # Application entry point
│   ├── config.py             # Configuration and env vars
│   ├── models.py             # SQLAlchemy models
│   ├── routes.py             # API endpoints (Blueprint)
│   ├── services.py           # Business logic and database operations
│   ├── requirements.txt      # Python dependencies
│   └── .env.example          # Example environment variables
├── frontend/                 # React (Vite) frontend
│   ├── src/
│   │   ├── api/              # Centralized Axios configuration
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/            # Page components (Home, About, Contact)
│   │   ├── styles/           # CSS files
│   │   ├── App.jsx           # App routing and layout
│   │   └── main.jsx          # React entry point
│   └── .env.example          # Example environment variables
├── README.md                 # Project documentation
└── .gitignore                # Ignored files
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the environment variables example file:
   ```bash
   cp .env.example .env
   ```
5. Run the Flask application:
   ```bash
   python app.py
   ```
   *The backend will run on `http://localhost:5000`. The SQLite database will be automatically created in `backend/instance/devconnect.db`.*

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install Node.js dependencies:
   ```bash
   npm install
   ```
3. Copy the environment variables example file:
   ```bash
   cp .env.example .env
   ```
4. Run the Vite development server:
   ```bash
   npm run dev
   ```
   *The frontend will typically run on `http://localhost:5173`. It will communicate with the backend via the `VITE_API_URL` environment variable.*

## API Endpoints (`/api/v1`)

- **GET `/api/v1/health`**: Returns application health status.
- **GET `/api/v1/about`**: Returns information about the application version and stack.
- **POST `/api/v1/contact`**: Accepts a JSON payload with `name`, `email`, and `message` to store in the database.

## Building for Production
To build the frontend for production, run:
```bash
cd frontend
npm run build
```
This generates static files in the `frontend/dist/` directory, which can be served by Nginx.
