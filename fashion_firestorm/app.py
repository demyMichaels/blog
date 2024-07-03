from flask import Flask, render_template, request

app = Flask(__name__)

# Define the crises, leadership styles, corporate cultures, and responses
crises = [
    "Cultural Insensitivity", "Racial Ads", "Miscommunication", "Poor Customer Service"
]
leadership_styles = ["Autocratic", "Democratic", "Laissez-Faire", "Transactional", "Transformational"]
corporate_cultures = ["Innovative", "Aggressive", "Outcome-Oriented", "Stable", "People-Oriented"]
responses = [
    "Apology", "Denial", "Excuse", "Justification", "Corrective Action", "Ingratiation"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        crisis = request.form.get('crisis')
        leadership_style = request.form.get('leadership_style')
        corporate_culture = request.form.get('corporate_culture')
        response = request.form.get('response')

        # For now, we'll just print the selected values. Later, we can add game logic here.
        print(f"Crisis: {crisis}")
        print(f"Leadership Style: {leadership_style}")
        print(f"Corporate Culture: {corporate_culture}")
        print(f"Response: {response}")

    return render_template('index.html', crises=crises, leadership_styles=leadership_styles, corporate_cultures=corporate_cultures, responses=responses)

if __name__ == '__main__':
    app.run(debug=True)
