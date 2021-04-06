from chalice import Chalice
import requests, json
import cbpro

from config import sandbox_b64secret as secret, sandbox_key as key, sandbox_secret as passphrase, ALPACA_SECRET_KEY as SECRET_KEY, ALPACA_API_KEY as API_KEY

ALPACA_BASE_URL = "https://paper-api.alpaca.markets"
CB_URL = "https://api.pro.coinbase.com"
CB_SBOX_URL = "https://api-public.sandbox.pro.coinbase.com"


app = Chalice(app_name='tradingview-webhook-alerts')
#auth_client = cbpro.AuthenticatedClient(sandbox_key, sandbox_b64secret, sandbox_secret, api_url=CB_SBOX_URL)
auth_client = cbpro.AuthenticatedClient(key, secret, passphrase, api_url=CB_SBOX_URL)

BTC_id = 'ecd6a272-67dbbbbbb0b-4453-aa19-2e9617ac2087'
USD_id = '93a22eef-7d25-43de-8f3c-cce834bd6c06'


#ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
#ORDERS_URL = "{}/v2/orders".format(ALPACA_BASE_URL)
#HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

#@app.route('/buy_stock', methods=['POST'])
#@app.route('/buy_stock')
@app.route('/buy', methods=['POST'])
def buy_stock():
	request = app.current_request
	webhook_message = request.json_body

	print(request)
	print(webhook_message)

	if webhook_message['action'] == 'buy':
            print("Buying $100 of BTC")
            auth_client.buy(product_id='BTC-USD', order_type='market', funds='100.0')
	elif webhook_message['action'] == 'sell':
            print("Selling  $100 of BTC")
            auth_client.sell(product_id='BTC-USD', order_type='market', funds='100.0')
	return
'''
	data =   {
		"symbol": webhook_message['ticker'],
		"qty": 1,
		"side": "buy",
		"type": "limit",
		"limit_price": webhook_message['close'],
		"time_in_force": "gtc",
		"order_class": "bracket",
		"take_profit": {
			"limit_price": webhook_message['close'] * 1.05
        },
        "stop_loss": {
            "stop_price": webhook_message['close'] * 0.98,
        }
    }
'''
	#r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
	
	#response = json.loads(r.content)
#	print(response)
#	print(response.keys())
#	return

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
