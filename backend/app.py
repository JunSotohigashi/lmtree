from flask import Flask

app = Flask(__name__)

counter = 0


@app.route("/")
def hello_world():
    global counter
    counter += 1
    return f"<p>Hello, World! <br /> Count: {counter}</p>"
