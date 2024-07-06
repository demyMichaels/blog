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
    for i in range(1, num_points):
        price_change = random.uniform(0.5, 1.5) * direction
        prices.append(prices[-1] + price_change)
        direction *= -1 if random.random() > 0.5 else 1
    return prices

def generate_volume_data(num_points):
    return [random.randint(100, 1000) for _ in range(num_points)]

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
    prices = generate_symmetric_triangle_prices(start_price, num_points)
    volumes = generate_volume_data(num_points)

    # Generate converging trendlines
    top_line = [max(prices[0], prices[-1]) - i * ((max(prices[0], prices[-1]) - min(prices[0], prices[-1])) / (num_points - 1)) for i in range(num_points)]
    bottom_line = [min(prices[0], prices[-1]) + i * ((max(prices[0], prices[-1]) - min(prices[0], prices[-1])) / (num_points - 1)) for i in range(num_points)]

    return {
        "dates": dates,
        "prices": prices,
        "volumes": volumes,
        "top_line": top_line,
        "bottom_line": bottom_line
    }

if __name__ == '__main__':
    app.run(debug=True)
