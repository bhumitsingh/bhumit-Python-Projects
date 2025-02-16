from flask import Flask, request, jsonify
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

app = Flask(__name__) # create a new instance of the Flask class

# Define Fuzzy Varibles
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Define fuzzy sets for the temperature
temperature['cold'] = fuzz.gbellmf(temperature.universe, 15, 3, 10)
temperature['warm'] = fuzz.gbellmf(temperature.universe, 20, 3, 50)
temperature['hot'] = fuzz.gbellmf(temperature.universe, 15, 3, 90)

# Define fuzzy sets for fan speed
fan_speed['slow'] = fuzz.gbellmf(fan_speed.universe, 15, 3, 10)
fan_speed['medium'] = fuzz.gbellmf(fan_speed.universe, 20, 3, 50)
fan_speed['fast'] = fuzz.gbellmf(fan_speed.universe, 15, 3, 90)

# Define IF-THEN Rules
rule1 = ctrl.Rule(temperature['cold'], fan_speed['slow'])
rule2 = ctrl.Rule(temperature['warm'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'], fan_speed['fast'])

# Create Fuzzy Control System
fan_control = ctrl.ControlSystem([rule1, rule2, rule3])
fan_sim = ctrl.ControlSystemSimulation(fan_control)

#Output Result
# print(f"At {temp_value}'C, the fan speed is: {fan_sim.output['fan_speed']:.2f}")

@app.route('/compute', methods=['POST'])
def compute_fan_speed():
    try:
        data = request.json
        temp_value = float(data['temperature'])
        fan_sim.input['temperature'] = temp_value
        fan_sim.compute()

        return jsonify({'temperature': temp_value, 'fan_speed': fan_sim.output['fan_speed']})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
    