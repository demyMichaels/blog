from flask import render_template, request
from app import app
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import io
import base64

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    initial_ebitda = float(request.form.get('initial_ebitda', 10))
    exit_multiple = float(request.form.get('exit_multiple', 5))
    exit_years = int(request.form.get('exit_years', 10))
    final_ebitda = initial_ebitda * 2
    
    debt_ratio = float(request.form.get('debt_ratio', 0.5))
    
    if debt_ratio not in [0, 0.5, 1]:
        debt_ratio = 0.5

    # Calculation logic
    equity_ratio = 1 - debt_ratio
    purchase_price = initial_ebitda * exit_multiple
    debt = purchase_price * debt_ratio
    equity = purchase_price * equity_ratio

    final_value = final_ebitda * exit_multiple
    annual_cash_flow = (final_value - debt) / exit_years

    # Calculate IRR
    cash_flows = [-equity] + [annual_cash_flow] * exit_years
    irr = np.irr(cash_flows)

    return render_template('./index.html', irr=irr, debt_ratio=debt_ratio)

def create_irr_chart():
    x = np.linspace(0, 20, 400)
    y = np.random.normal(loc=10, scale=2, size=400)
    fig = go.Figure(data=[go.Histogram(x=y, nbinsx=50)])

    fig.update_layout(
        title="IRR Distribution",
        xaxis_title="IRR (%)",
        yaxis_title="Frequency",
        shapes=[
            dict(
                type="line",
                x0=7,
                y0=0,
                x1=7,
                y1=0.15,
                line=dict(color="Red", width=3),
            )
        ],
        annotations=[
            dict(
                x=7,
                y=0.15,
                xref="x",
                yref="y",
                text="7% hurdle",
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-40,
            )
        ]
    )
    return fig

@app.route('chart.html')
def chart():
    fig = create_irr_chart()
    img_bytes = fig.to_image(format="png")
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    return render_template('chart.html', chart=img_base64)
