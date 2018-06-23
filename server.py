from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

response_entity = '{"conversationToken":"","expectUserResponse":true,"expectedInputs":[{"inputPrompt":{"richInitialPrompt":{"items":[{"simpleResponse":{"textToSpeech":"Mathandprimenumbersitis!"}},{"basicCard":{"title":"Math&primenumbers","formattedText":"42isanevencompositenumber.It\niscomposedofthreedistinctprimenumbersmultipliedtogether.It\nhasatotalofeightdivisors.42isanabundantnumber,becausethe\nsumofitsproperdivisors54isgreaterthanitself.Tocountfrom\n1to42wouldtakeyouabouttwenty-one…","image":{"url":"https://example.google.com/42.png","accessibilityText":"Imagealternatetext"},"buttons":[{"title":"Readmore","openUrlAction":{"url":"https://example.google.com/mathandprimes"}}],"imageDisplayOptions":"CROPPED"}}],"suggestions":[]}},"possibleIntents":[{"intent":"actions.intent.TEXT"}]}]}'

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
