from flask import Flask, render_template
import requests
import time
import json
import threading

global response_b
global response_t
global response_g



def req_Battery():
    url_items = "http://192.168.50.94:8000/Vehicle/Battery"
    while True:
        global response_b
        response_b = requests.get(url_items)
        if "r1ID" in response_b.text:
            print(response_b.text)
            #print(type(json.loads(response.text)))
        time.sleep(1)


def req_Temperature():
    url_items = "http://192.168.50.94:8000/Vehicle/Temperature"
    while True:
        global response_t
        response_t = requests.get(url_items)
        if "r1ID" in response_t.text:
            print(response_t.text)
        time.sleep(1)


def req_GPosition():
    url_items = "http://192.168.50.94:8000/Vehicle/Gposition"
    while True:
        global response_g
        response_g = requests.get(url_items)
        if "r1ID" in response_g.text:
            print(response_g.text)
        time.sleep(1)


data_B = threading.Thread(target=req_Battery)
data_B.start()

data_T = threading.Thread(target=req_Temperature)
data_T.start()

data_G = threading.Thread(target=req_GPosition)
data_G.start()

app = Flask(__name__)


@app.route('/Battery')
def get_Battery():
    if "r1ID" in response_b.text:
        print(response_b.text)
        return render_template('Battery.html', data=json.loads(response_b.text))


@app.route('/Temperature')
def get_Temperature():
    if "r1ID" in response_t.text:
        print(response_t.text)
        return render_template('Temperature.html', data=json.loads(response_t.text))


@app.route('/GPosition')
def get_GPosition():
    if "r1ID" in response_g.text:
        print(response_g.text)
        return render_template('GPosition.html', data=json.loads(response_g.text))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="9999")
