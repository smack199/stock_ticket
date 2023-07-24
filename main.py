from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def stock_price():
    price = None
    if request.method == 'POST':
        stock_symbol = request.form.get('symbol')
        api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'  # Dummy Key for Now!
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        price = data["Global Quote"]["05. price"]
    return render_template('index.html', price=price)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
