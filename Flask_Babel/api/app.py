from flask import Flask, request, jsonify
from flask_babel import Babel, format_date, gettext
from datetime import date

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'es'
babel = Babel(app)

def get_locale():
    return request.accept_languages.best_match(['en', 'es', 'de'])

@app.route('/api/v1/')
def user():
    login_date = date(2024, 7, 2)
    return jsonify({gettext('user'): 'Taya', 'loginDate': format_date(login_date)})

if __name__ == '__main__':
    app.run(debug=True)
