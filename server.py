import logging
import webbrowser
from logging.handlers import RotatingFileHandler
from picamera import PiCamera
from time import sleep

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

response_entity = '{"textToSpeech":"test","ssml":"","displayText":"test"}'

def send_static(path):
        return send_from_directory('static', path)

def camera(request):
    app.logger.info('Executing camera intent')
    camera = PiCamera()
    camera.start_preview()
    return 'camera'

def stop_camera():
    camera = PiCamera()
    camera.stop_preview()
    return ''

def directions(request):
    app.logger.info('Executing directions intent')
    url = "https://maps.google.com"
    chrome_path = '/usr/bin/chromium-browser %s'
    webbrowser.get(chrome_path).open(url)
    return 'directions'

def handle(request):
    app.logger.info('Handling intent')
    json = request.get_json()
    intent = json["queryResult"]["intent"]["displayName"];
    
    #stop the camera preview
    stop_camera()

    if (intent == "directions"):
        directions(request)
    elif (intent == "camera"):
        camera(request)

    app.logger.info(intent)
    return ''

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
        handle(request)            
        return 'intent handled'

if __name__ == "__main__":
    handler = RotatingFileHandler('TSG.log', maxBytes=100000, backupCount=1)
    # Loger logs at info level and above
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    app.run(host='0.0.0.0', port=80, debug=True)

