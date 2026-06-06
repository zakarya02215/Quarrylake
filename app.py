from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

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
        
        resp = jsonify(response.json())
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
