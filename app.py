from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Temporary storage of registered users (email: {name, password})
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loginyt')
def loginyt():
    return render_template('loginyt.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    if not name or not email or not password:
        flash("All fields are required for registration!")
        return redirect(url_for('loginyt'))

    if email in users:
        flash("This email is already registered. Please log in.")
        return redirect(url_for('loginyt'))

    # Save the new user
    users[email] = {'name': name, 'password': password}
    flash("Registration successful! Please log in.")
    return redirect(url_for('loginyt'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        flash("Please enter both email and password.")
        return redirect(url_for('loginyt'))

    user = users.get(email)
    if user and user['password'] == password:
        return redirect(url_for('afterlogin'))
    else:
        flash("Invalid email or password. Please try again or register.")
        return redirect(url_for('loginyt'))

@app.route('/afterlogin')
def afterlogin():
    return render_template('afterlogin.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
