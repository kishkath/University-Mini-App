# University Issue Tracking System

A simple web application that allows university students to submit and track their issues/concerns. Built with Flask backend and vanilla HTML/CSS/JavaScript frontend.

## Prerequisites

Before you begin, ensure you have Python 3.x installed on your system.

### Checking Python Installation

```bash
python --version  # or python3 --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/)

## Project Setup

1. Create the project directory structure:
```bash
mkdir university-issue-tracker
cd university-issue-tracker
```

2. Create the following directory structure:
```
backend/
    ├── static/
    │   ├── style.css
    │   └── script.js
    ├── templates/
    │   └── index.html
    └── app.py
```

## Installation Steps

1. Create a virtual environment:
```bash
# Windows
python -m venv venv

# Linux/MacOS
python3 -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/MacOS
source venv/bin/activate
```

3. Install required packages:
```bash
pip install flask
```

## Running the Application

1. Make sure you're in the project directory with the virtual environment activated

2. Navigate to the backend directory:
```bash
cd backend
```

3. Run the Flask application:
```bash
# Windows
python app.py

# Linux/MacOS
python3 app.py
```

4. Open your web browser and visit:
```
http://localhost:5000
```

## Using the Application

1. Fill out the form with:
   - Full Name
   - Student ID
   - Email
   - Problem Description
   - Suggested Solution

2. Click "Submit Issue" to submit your concern

3. View all submitted issues in the "Recent Issues" section below the form

## Troubleshooting

If you encounter any issues:

1. Ensure Python is correctly installed
2. Verify that Flask is installed in your virtual environment
3. Check if the virtual environment is activated
4. Make sure all files are in their correct directories
5. Check the console for any error messages

## File Structure Explanation

- `app.py`: Main Flask application file
- `static/style.css`: Contains all styling for the application
- `static/script.js`: Contains frontend JavaScript code
- `templates/index.html`: Main HTML template
- `issues.db`: SQLite database file (created automatically)

## Database

The application uses SQLite database which will be created automatically when you first run the application. No additional database setup is required.

## Development

To modify the application:
- Frontend code is in the `templates` and `static` directories
- Backend code is in `app.py`
- Database schema is defined in the `init_db()` function in `app.py`

## Security Note

This is a basic implementation for demonstration purposes. For production use, additional security measures should be implemented:
- Input validation
- CSRF protection
- SQL injection prevention
- Error handling
- User authentication 