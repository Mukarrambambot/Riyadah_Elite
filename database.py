# database.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Modify this according to your database configuration
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

def export_signup_login_to_excel():
    users = User.query.all()
    user_data = [(user.username, user.email, user.password) for user in users]
    df = pd.DataFrame(user_data, columns=['Username', 'Email', 'Password'])
    df.to_excel('signup_login.xlsx', index=False)

def login(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        return True
    else:
        return False

if __name__ == '__main__':
    export_signup_login_to_excel()
