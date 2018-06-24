import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

response_entity = '{"textToSpeech":"test","ssml":"","displayText":"test"}'

def send_static(path):
        return send_from_directory('static', path)

@app.route("/", methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET': 
        app.logger.warning('A warning occurred (%d apples)', 42)
        app.logger.error('An error occurred')
        app.logger.info('Info')
        templateData = {
            'title' : 'HELLO!',
            'time': 'time o clock' 
        }
        return render_template('dashboard.html', **templateData)
    else: 
        app.logger.info('test logged in successfully')
        app.logger.warning('A warning occurred (%d apples)', 42)
        app.logger.error('An error occurred')
        app.logger.info('Info')
        return 'message'

if __name__ == "__main__":
    handler = RotatingFileHandler('TSG.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    app.run(host='0.0.0.0', port=8000, debug=True)

