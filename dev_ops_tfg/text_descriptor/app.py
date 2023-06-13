from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def show_text():
    text = request.form['text']
    return render_template('index.html', text=text)

# PORT = int(os.environ.get('PORT', 5000))
PORT = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
    # app.run(host='0.0.0.0', port=666, debug=True)
    # app.run(host="0.0.0.0")

