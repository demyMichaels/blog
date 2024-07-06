// Function to update gauges based on inputs
function updateGauges() {
    const riskLevel = document.getElementById('risk-level-input').value;
    const returnLevel = document.getElementById('return-potential-input').value;
    const timeHorizon = document.getElementById('time-horizon-input').value;

    const speedometerGauge = document.getElementById('speedometer');
    const fuelGauge = document.getElementById('fuel-gauge');
    const odometer = document.getElementById('odometer');

    speedometerGauge.style.transform = `scale(${riskLevel / 100})`;
    fuelGauge.style.transform = `scale(${returnLevel / 100})`;
    odometer.style.transform = `scale(${timeHorizon / 100})`;

    speedometerGauge.querySelector('.gauge-value').textContent = riskLevel;
    fuelGauge.querySelector('.gauge-value').textContent = returnLevel;
    odometer.querySelector('.gauge-value').textContent = timeHorizon;
}

// Initial update
updateGauges();

// Add event listeners to input fields
document.getElementById('risk-level-input').addEventListener('input', updateGauges);
document.getElementById('return-potential-input').addEventListener('input', updateGauges);
document.getElementById('time-horizon-input').addEventListener('input', updateGauges);
