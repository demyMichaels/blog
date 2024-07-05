from flask import Flask, render_template, jsonify
import numpy as np
import datetime
import random

app = Flask(__name__)

def generate_date_range(start_date, num_days):
    return [start_date + datetime.timedelta(days=i) for i in range(num_days)]

def generate_symmetric_triangle_prices(start_price, num_points):
    prices = [start_price]
    direction = 1
    for _ in range(1, num_points):
        price_change = random.uniform(0.5, 1.5) * direction
        prices.append(prices[-1] + price_change)
        direction *= -1 if random.random() > 0.5 else 1
    return prices

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_chart_data')
def get_chart_data():
    data = generate_symmetrical_triangle_data()
    return jsonify(data)

def generate_symmetrical_triangle_data():
    # Generate date range
    num_points = 20
    start_date = datetime.datetime.now()
    dates = generate_date_range(start_date, num_points)

    # Generate symmetric triangle prices
    start_price = 100
    uptrend_prices = generate_symmetric_triangle_prices(start_price, num_points)
    downtrend_prices = generate_symmetric_triangle_prices(start_price, num_points)

    # Converging lines for uptrend
    uptrend_converge = {
        "dates": [dates[0], dates[-1]],
        "top_line": [uptrend_prices[0], uptrend_prices[-1]],
        "bottom_line": [uptrend_prices[0], uptrend_prices[-1]]
    }

    # Converging lines for downtrend
    downtrend_converge = {
        "dates": [dates[0], dates[-1]],
        "top_line": [downtrend_prices[0], downtrend_prices[-1]],
        "bottom_line": [downtrend_prices[0], downtrend_prices[-1]]
    }

    return {
        "uptrend": {"dates": dates, "prices": uptrend_prices},
        "downtrend": {"dates": dates, "prices": downtrend_prices},
        "uptrend_converge": uptrend_converge,
        "downtrend_converge": downtrend_converge
    }

if __name__ == '__main__':
    app.run(debug=True)
