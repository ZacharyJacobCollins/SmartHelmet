from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

response_entity = '{ "conversationToken": "", "expectUserResponse": true, "expectedInputs": [ { "inputPrompt": { "richInitialPrompt": { "items": [ { "simpleResponse": { "textToSpeech": "Math and prime numbers it is!" } }, { "basicCard": { "title": "Math & prime numbers", "formattedText": "42 is an even composite number. It\n is composed of three distinct prime numbers multiplied together. It\n has a total of eight divisors. 42 is an abundant number, because the\n sum of its proper divisors 54 is greater than itself. To count from\n 1 to 42 would take you about twenty-one…", "image": { "url": "https://example.google.com/42.png", "accessibilityText": "Image alternate text" }, "buttons": [ { "title": "Read more", "openUrlAction": { "url": "https://example.google.com/mathandprimes" } } ], "imageDisplayOptions": "CROPPED" } } ], "suggestions": [] } }, "possibleIntents": [ { "intent": "actions.intent.TEXT" } ] } ] }'

@app.route('/static/<path:path>')
def send_static(path):
        return send_from_directory('static', path)

@app.route("/", methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET': 
        templateData = {
            'title' : 'HELLO!',
            'time': 'time o clock' 
        }
        return render_template('dashboard.html', **templateData)
    else: 
        return jsonify(response_entity)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
