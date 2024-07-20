from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hi there, Space QBee!"


if __name__ == '__main__':
    app.run(debug=True)
