import logging
from logging.handlers import RotatingFileHandler
from picamera import PiCamera
from time import sleep

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

response_entity = '{"textToSpeech":"test","ssml":"","displayText":"test"}'

def send_static(path):
        return send_from_directory('static', path)

@app.route("/", methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET': 
        app.logger.info('Serving dashboard page')
        templateData = {
            'title' : 'HELLO!',
            'time': 'time o clock' 
        }
        return render_template('dashboard.html', **templateData)
    else: 
        app.logger.info('Responding to directions request')
        return 'directions are'

@app.route("/camera", methods=['POST'])
def camera():
    camera = PiCamera()
    camera.start_preview()
    #camera.stop_preview()
    return 'camera'

if __name__ == "__main__":
    handler = RotatingFileHandler('TSG.log', maxBytes=100000, backupCount=1)
    # Loger logs at info level and above
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    app.run(host='0.0.0.0', port=8000, debug=True)

