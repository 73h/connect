import time

from flask import Flask, render_template, make_response

app = Flask(__name__)


def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)


@app.get('/')
def index():
    context = {'server_time': format_server_time()}
    template = render_template('index.html', context=context)
    response = make_response(template)
    response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
    return response
