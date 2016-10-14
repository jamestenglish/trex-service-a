from flask import Flask, send_from_directory
from demo import ANSWER
from version import VERSION
import time
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Trex Service A'

@app.route('/demo')
def demo():
    time.sleep(1)
    return str(ANSWER)

@app.route('/v')
def v():
    return str(VERSION)

@app.route('/health')
def health():
    return 'healthy'

@app.route('/test')
def test():
    is_testing = os.getenv('IS_TESTING', False)
    
    if not is_testing:
        return "no"
    try:
        return send_from_directory('results', 'nose2-junit.xml')
    finally:
        import sys
        sys.exit()


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=8080)

