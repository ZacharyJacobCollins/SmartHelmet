from flask import Flask, render_template, request

app = Flask(__name__)

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
        return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
