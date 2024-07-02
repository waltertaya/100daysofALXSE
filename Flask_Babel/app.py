from flask import Flask, render_template
from flask_babel import numbers, dates
from datetime import datetime, date, time

app = Flask(__name__)

@app.route('/')
def index():
    us_number = numbers.format_decimal(1.2367, locale='en_US') # usa
    se_number = numbers.format_decimal(1.2367, locale='sv_SE') # sweden
    de_number = numbers.format_decimal(1.2367, locale='de_DE') # Germany

    us_whole = numbers.format_decimal(12367, locale='en_US') # usa
    se_whole = numbers.format_decimal(12367, locale='sv_SE') # sweden
    de_whole = numbers.format_decimal(12367, locale='de_DE') # Germany
    results = {'us_num': us_number, 'se_num': se_number, 'de_num': de_number, 'us_whole': us_whole, 'se_whole': se_whole, 'de_whole': de_whole}
    return render_template('index.html', results=results)

@app.route('/dates')
def home():
    my_date = date(2002, 5, 22)
    my_dt = datetime(2024, 7, 2, 14, 59)

    us_date = dates.format_date(my_date, locale='en_US')
    de_date = dates.format_date(my_date, locale='de_DE')

    us_dt = dates.format_datetime(my_dt, locale='en_US')
    de_dt = dates.format_datetime(my_dt, locale='de_DE')

    context = { 'us_date': us_date, 'de_date': de_date, 'us_dt': us_dt, 'de_dt': de_dt }

    return render_template('home.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
