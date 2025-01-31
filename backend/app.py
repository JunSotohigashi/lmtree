from flask import Flask

app = Flask(__name__)

counter = 0


@app.route("/")
def hello_world():
    global counter
    counter += 1
    return {"message": f"Hello, World! count={counter}"}
