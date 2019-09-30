from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/list', methods=['POST', 'GET'])
def list():
    data = ""
    if request.args.get('s') and request.args.get('f'):
        startdate = request.args.get('s')
        finishdate = request.args.get('f')
        App_token = "app_token=ag9zfnRlbGVmb25pLXRlc3RyHwsSElRlbmFudEFwcGxpY2F0aW9ucxiAgICw46OcCQyiARVzdGFnaW5nMS5hbG8tdGVjaC5jb20"
        url = "http://staging1.alo-tech.com/api/?function=reportsCDRLogs&startdate={}%2012:00:00&finishdate={}%2013:00:00&{}"\
            .format(startdate, finishdate, App_token)
        r = requests.get(url)
        data = r.json()

    return render_template('list.html', tasks=data)


if __name__ == "__main__":
    app.run(debug=True)
