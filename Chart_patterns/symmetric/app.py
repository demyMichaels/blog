from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_chart_data')
def get_chart_data():
    data = generate_symmetrical_triangle_data()
    return jsonify(data)

def generate_symmetrical_triangle_data():
    # Generate the data for symmetrical triangle charts
    uptrend = {
        "x": [1, 2, 3, 4, 5],
        "y": [1, 20, 5, 10, 20]
    }
    downtrend = {
        "x": [1, 2, 3, 4, 5, 6],
        "y": [5, 3, 4, 2, 3, 1]
    }
    return {"uptrend": uptrend, "downtrend": downtrend}

if __name__ == '__main__':
    app.run(debug=True)
