import matplotlib.pyplot as plt
from io import BytesIO
import base64
from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

# Data
scenarios = ["Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", "Scenario 5"]
probabilities = [0.20, 0.50, 0.30, 0.25, 0.45]
stock_devs = [-0.14, -0.04, 0.16, 0.12, -0.08]
call_devs = [-1.50, -1.50, 3.50, 1.80, -2.00]
put_devs = [0.825, 0.75, -0.675, 0.90, 1.20]

squared_stock_devs = [x**2 for x in stock_devs]
squared_call_devs = [x**2 for x in call_devs]
squared_put_devs = [x**2 for x in put_devs]

product_stock_call = [stock_devs[i] * call_devs[i] for i in range(len(stock_devs))]
product_stock_put = [stock_devs[i] * put_devs[i] for i in range(len(stock_devs))]
product_call_put = [call_devs[i] * put_devs[i] for i in range(len(stock_devs))]

# Weigh products by probabilities
weighted_products = {
    'Stock-Call': sum(product_stock_call[i] * probabilities[i] for i in range(len(product_stock_call))),
    'Stock-Put': sum(product_stock_put[i] * probabilities[i] for i in range(len(product_stock_put))),
    'Call-Put': sum(product_call_put[i] * probabilities[i] for i in range(len(product_call_put))),
}

# Find the most profitable and likely recommendation
max_product_key = max(weighted_products, key=weighted_products.get)
max_product_value = weighted_products[max_product_key]

# Find the box with the least exposure to correlation risk
correlation_risk = np.abs(np.array(product_stock_call) + np.array(product_stock_put) + np.array(product_call_put))
min_correlation_risk_index = np.argmin(correlation_risk)

def create_heatmap():
    data = [product_stock_call, product_stock_put, product_call_put]
    fig, ax = plt.subplots()
    cax = ax.imshow(data, cmap='hot', interpolation='nearest', aspect='auto')
    ax.set_xticks(range(len(scenarios)))
    ax.set_xticklabels(scenarios)
    ax.set_yticks(range(3))
    ax.set_yticklabels(['Stock-Call', 'Stock-Put', 'Call-Put'])
    
    # Highlight the most profitable and likely recommendation
    row_max = ['Stock-Call', 'Stock-Put', 'Call-Put'].index(max_product_key)
    col_max = probabilities.index(max(probabilities))
    rect_max = plt.Rectangle((col_max - 0.5, row_max - 0.5), 1, 1, fill=False, edgecolor='blue', linewidth=3)
    ax.add_patch(rect_max)

    # Highlight the box with the least exposure to correlation risk
    row_min_corr = min_correlation_risk_index
    col_min_corr = np.argmin(correlation_risk)
    rect_min_corr = plt.Rectangle((col_min_corr - 0.5, row_min_corr - 0.5), 1, 1, fill=False, edgecolor='green', linewidth=3)
    ax.add_patch(rect_min_corr)

    cbar = fig.colorbar(cax)
    cbar.set_ticks([-2, -1, 0, 1, 2])
    cbar.set_ticklabels(['Very Low Significance', 'Low Significance', 'Moderate Significance', 'High Significance', 'Very High Significance'])
    plt.title('Heatmap of Product of Deviations')

    # Add annotation below the heatmap
    plt.figtext(0.5, -0.1, 'Blue border indicates the most profitable and likely recommendation\nGreen border indicates the least exposure to correlation risk', ha='center', fontsize=12, color='blue')

    return plt_to_base64()

def plt_to_base64():
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

@app.route('/')
def index():
    heatmap_img = create_heatmap()
    return render_template('index.html', heatmap_img=heatmap_img)

if __name__ == '__main__':
    app.run(debug=True)
