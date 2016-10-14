from flask import Flask
from demo import ANSWER
from version import VERSION
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/demo')
def demo():
    time.sleep(1)
    return ANSWER

@app.route('/v')
def v():
    return VERSION

@app.route('/health')
def health():
    return 'healthy'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=8080)

