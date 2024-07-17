from flask import Flask
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    "secret-token-1": "brett",
    "secret-token-2": "taya"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

if __name__ == '__main__':
    app.run()
