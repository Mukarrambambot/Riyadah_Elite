# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from database import login

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/tournaments')
def tournaments():
    return render_template('tournaments.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup_login', methods=['GET', 'POST'])
def signup_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login(username, password):
            # Redirect user to a logged-in page
            return redirect(url_for('index'))
        else:
            # Display an error message for unsuccessful login
            flash('Invalid username or password. Please try again.', 'error')
            return redirect(url_for('signup_login'))
    else:
        return render_template('signup_login.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001, use_reloader=False)
