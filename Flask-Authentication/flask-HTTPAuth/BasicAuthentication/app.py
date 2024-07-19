from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

import os

app = Flask(__name__)
auth = HTTPBasicAuth()

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=os.getenv('POSTGRES_USER'),pw=os.getenv('POSTGRES_PW'),url=os.getenv('POSTGRES_URL'),db=os.getenv('POSTGRES_DB'))

print(DB_URL)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

users = {
    'brett': generate_password_hash('cooper'),
    'taya': generate_password_hash('waltertaya')
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/')
@auth.login_required
def index():
    return f'Hello, {auth.current_user()}!'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
