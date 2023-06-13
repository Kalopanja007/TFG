from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def show_text():
    text = request.form['text']
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # app.run(host="0.0.0.0")

