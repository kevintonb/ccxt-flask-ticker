# -*- coding: utf-8 -*-

import ccxt  # noqa: E402
from flask import *
import json

app = Flask(__name__)
exchanges = {}  # a placeholder for your instances

for id in ccxt.exchanges:
    exchange = getattr(ccxt, id)
    exchanges[id] = exchange()

@app.route('/')
def dropdown():
	return render_template('index.html',base = exchanges)

@app.route('/ticker/<exchange>/<symbol1>/<symbol2>', methods=['GET'])
def get_ticker(exchange,symbol1,symbol2):
    return jsonify(exchanges[exchange].fetch_ticker(symbol1+"/"+symbol2))

#@app.route('/okcoin', methods=['GET'])
#def get_exchanges():
#	okcoin = ccxt.okcoinusd()
	#markets = okcoin.load_markets()

if __name__ == '__main__':
    app.run(debug = True)