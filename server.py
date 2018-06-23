from flask import Flask, render_template, request

app = Flask(__name__)

response_entity = { "conversationToken":"[]", "expectUserResponse":true, "expectedInputs":[ { "inputPrompt":{ "richInitialPrompt":{ "items":[ { "simpleResponse":{ "textToSpeech":"WelcometoPass" } } ] } }, "possibleIntents":[ { "intent":"assistant.intent.action.TEXT" } ] } ], "responseMetadata":{ "status":{ "message":"Success(200)" }, "queryMatchInfo":{ "queryMatched":true, "intent":"2379c8dd-f563-40ca-8da2-401cb2f2a2bb" } } }

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
<<<<<<< HEAD
        return response_entity
=======
        return ''
>>>>>>> 2466c2c4388a2385eed756c8484a30c6a93845cf

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
