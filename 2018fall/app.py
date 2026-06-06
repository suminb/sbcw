from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/test')
def test():
    return 'This is a test'


app.run(port=8050, debug=True)
