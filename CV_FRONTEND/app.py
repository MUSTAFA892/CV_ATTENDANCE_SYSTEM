from flask import Flask, request, jsonify, render_template, redirect, url_for
from firebase_admin import auth
import firebase_config  # This initializes Firebase
import sqlite3  # For database operations

app = Flask(__name__)

# Route to login page
@app.route('/')
def index():
    return render_template('login.html')

# Route to verify Firebase token
@app.route('/verify', methods=['POST'])
def verify_token():
    id_token = request.json.get('idToken')
    try:
        decoded_token = auth.verify_id_token(id_token)
        print(f"Decoded token: {decoded_token}")
        return jsonify({"status": "Token verified"}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Invalid or expired token"}), 401

# Route to dashboard with database data
@app.route('/dashboard')
def dashboard():
    # Connect to SQLite3 database
    conn = sqlite3.connect('../CV_Attendance/attendance.db')  # Update with your database path
    cursor = conn.cursor()

    # Retrieve attendance data
    cursor.execute("SELECT * FROM attendance")  # Assuming table is named 'attendance'
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Pass data to template
    return render_template('dashboard.html', data=rows)

if __name__ == '__main__':
    app.run(debug=True)
