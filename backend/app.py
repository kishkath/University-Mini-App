from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATABASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'issues.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    try:
        os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
        
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS issues (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                student_id TEXT NOT NULL,
                email TEXT NOT NULL,
                problem TEXT NOT NULL,
                solution TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        print(f"Database initialized successfully at {DATABASE_PATH}")
    except Exception as e:
        print(f"Error initializing database: {str(e)}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_issue', methods=['POST'])
def submit_issue():
    try:
        print("Received data:", request.json)
        
        data = request.json
        if not all(key in data for key in ['name', 'studentId', 'email', 'problem']):
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        c = conn.cursor()
        
        solution = data.get('solution', '')
        
        print("Inserting data:", (
            data['name'],
            data['studentId'],
            data['email'],
            data['problem'],
            solution
        ))
        
        c.execute('''
            INSERT INTO issues (name, student_id, email, problem, solution)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            data['name'],
            data['studentId'],
            data['email'],
            data['problem'],
            solution
        ))
        conn.commit()
        conn.close()
        
        print("Data inserted successfully")
        return jsonify({"message": "Issue submitted successfully"}), 200
    except Exception as e:
        print(f"Error in submit_issue: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/get_issues', methods=['GET'])
def get_issues():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM issues ORDER BY created_at DESC')
        issues = c.fetchall()
        
        issues_list = []
        for issue in issues:
            issues_list.append({
                'id': issue[0],
                'name': issue[1],
                'student_id': issue[2],
                'email': issue[3],
                'problem': issue[4],
                'solution': issue[5] or '',
                'created_at': issue[6]
            })
        conn.close()
        return jsonify(issues_list)
    except Exception as e:
        print(f"Error in get_issues: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)