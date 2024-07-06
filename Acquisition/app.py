from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    acquisition_type = request.form['acquisition_type']
    initial_ebitda = float(request.form['initial_ebitda'])
    exit_multiple = float(request.form['exit_multiple'])
    exit_years = int(request.form['exit_years'])
    final_ebitda = float(request.form['final_ebitda'])
    
    # Simulate based on acquisition_type
    result = simulate_acquisition(acquisition_type, initial_ebitda, exit_multiple, exit_years, final_ebitda)
    return render_template('result.html', result=result)

def simulate_acquisition(acquisition_type, initial_ebitda, exit_multiple, exit_years, final_ebitda):
    if acquisition_type == 'half_debt_half_equity':
        equity_investment = initial_ebitda * 2.5  # 50% of the total investment
        debt = initial_ebitda * 2.5  # 50% of the total investment
    elif acquisition_type == 'full_debt':
        equity_investment = 0
        debt = initial_ebitda * 5
    elif acquisition_type == 'full_equity':
        equity_investment = initial_ebitda * 5
        debt = 0
    
    exit_value = final_ebitda * exit_multiple
    equity_value = exit_value - debt
    irr = (equity_value / equity_investment) ** (1/exit_years) - 1
    
    return {
        'initial_ebitda': initial_ebitda,
        'final_ebitda': final_ebitda,
        'exit_value': exit_value,
        'equity_value': equity_value,
        'irr': irr * 100  # Convert to percentage
    }

if __name__ == '__main__':
    app.run(debug=True)
