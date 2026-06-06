from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "QuarryLake API is running!"

@app.route('/api/klines')
def get_klines():
    try:
        symbol = request.args.get('symbol', 'XAUUSDT')
        interval = request.args.get('interval', '15m')
        limit = request.args.get('limit', '200')
        
        url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
        response = requests.get(url, timeout=10)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/price')
def get_price():
    try:
        symbol = request.args.get('symbol', 'XAUUSDT')
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
        response = requests.get(url, timeout=10)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
