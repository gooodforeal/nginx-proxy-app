from flask import Flask, render_template, request
import requests
import urllib.parse

app = Flask(__name__)


WOLFRAM_ALPHA_APPID = '5Y2AYK-7YX89VEL8K'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        url = "http://192.168.1.7:90/proxy"

        response = requests.get(url)

        if response.status_code == 200:
            result = response.text
            return render_template('index.html', result=result)
        else:
            return render_template('index.html', error=f"Ошибка: {response.status_code}")
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


