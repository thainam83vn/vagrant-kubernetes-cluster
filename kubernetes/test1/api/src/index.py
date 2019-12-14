import flask
from flask import request, jsonify
from stock_service import StockService
app = flask.Flask(__name__)
app.config["DEBUG"] = True

api = StockService()

@app.route('/', methods = ['GET'])
def home():
    return jsonify({"symbol":"SNAP"})

@app.route('/api/suggestions', methods=['GET'])
def apiStockSuggestions():
    result = api.suggestions()
    return jsonify(result)

app.run()