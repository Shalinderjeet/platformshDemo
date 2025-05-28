from flask import Flask
app = Flask(__name__)
#hello
@app.route('/')
def hello():
    return 'Hello, World from Platform.sh!'
