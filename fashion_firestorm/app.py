import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Define crises, response categories, and initial setup
crises = [
    "Cultural Insensitivity", "Racial Ads", "Miscommunication", "Poor Customer Service"
]
response_phases = [
    {"name": "First Response", "sentiment_impact": random.randint(-10, 10)},
    {"name": "Second Response", "sentiment_impact": random.randint(-10, 10)},
    {"name": "Third Response", "sentiment_impact": random.randint(-10, 10)}
]
leadership_styles = ["Autocratic", "Democratic", "Laissez-Faire", "Transactional", "Transformational"]
corporate_cultures = ["Innovative", "Aggressive", "Outcome-Oriented", "Stable", "People-Oriented"]
responses = [
    "Apology", "Denial", "Excuse", "Justification", "Corrective Action", "Ingratiation"
]

current_phase_index = 0  # Track the current response phase index

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_phase_index

    selected_crisis = crises[random.randint(0, len(crises) - 1)]
    current_phase = response_phases[current_phase_index]

    if request.method == 'POST':
        leadership_style = request.form.get('leadership_style')
        corporate_culture = request.form.get('corporate_culture')
        response = request.form.get('response')

        # Simulate impact on sentiment based on current phase's impact
        sentiment_impact = current_phase['sentiment_impact']
        # Update the current crisis scenario based on sentiment impact (simulation logic)
        # Example: Update sentiment and crisis scenario based on impact

        # Move to the next phase after handling the current one
        current_phase_index += 1
        if current_phase_index >= len(response_phases):
            # Game ends, calculate final score or display results
            return render_template('game_end.html')

    return render_template('index.html', crisis=selected_crisis, phase=current_phase, leadership_styles=leadership_styles, corporate_cultures=corporate_cultures, responses=responses)

if __name__ == '__main__':
    app.run(debug=True)
