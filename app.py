from flask import Flask, render_template, request, redirect, session, url_for
from utils.db import get_db, init_db
from utils.hash import hash_password, check_password
from utils.auth import generate_secret, verify_otp
import pyotp

app = Flask(__name__)
app.secret_key = "supersecretkey"

init_db()

@app.route('/')
def home():
    if 'user' in session:
        return redirect('/dashboard')
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed = hash_password(password)
        secret = generate_secret()

        conn = get_db()
        try:
            conn.execute(
                "INSERT INTO users (username, password, secret) VALUES (?, ?, ?)",
                (username, hashed, secret)
            )
            conn.commit()
        except:
            return "User already exists"

        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        otp = request.form.get('otp')

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()

        if user and check_password(password, user['password']):
            if user['secret']:
                if not otp or not verify_otp(user['secret'], otp):
                    return "Invalid OTP"

            session['user'] = username
            return redirect('/dashboard')

        return "Invalid credentials"

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)
