from flask import Flask, jsonify

app = Flask(__name__)

exchange_rates = {
    "TWD": {
        "TWD": 1,
        "JPY": 3.669,
        "USD": 0.03281
    },
    "JPY": {
        "TWD": 0.26956,
        "JPY": 1,
        "USD": 0.00885
    },
    "USD": {
        "TWD": 30.444,
        "JPY": 111.801,
        "USD": 1
    }
}

@app.route('/exchange', methods=['POST'])
def exchange():
  data = request.get_json()

  if not data or 'source' not in data or 'target' not in data or 'amount' not in data:
    return jsonify({'msg': 'Invalid request data. Please provide source, target, and amount.', 'amount': 0.0}), 400

  source = data['source'].upper()
  target = data['target'].upper()
  amount = float(data['amount'])

  if source not in exchange_rates or target not in exchange_rates:
    return jsonify({'msg': 'Invalid currency code provided.', 'amount': 0.0}), 400

  if source == target:
    return jsonify({'msg': 'Same currency conversion not supported.', 'amount': amount}), 400

  conversion_rate = exchange_rates[source][target]
  converted_amount = amount * conversion_rate

  # Round the converted amount to two decimal places
  converted_amount = round(converted_amount, 2)

  return jsonify({'msg': 'Exchange successful!', 'amount': converted_amount}), 200

if __name__ == '__main__':
  app.run(debug=True)
