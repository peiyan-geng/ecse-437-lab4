from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')

    if not all([num1, num2, operation]):
        return jsonify({'error': 'Missing data'}), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter numeric values.'}), 400

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)