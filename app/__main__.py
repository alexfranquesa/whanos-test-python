from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return 'Hello Pol! This is '

app.run(host='0.0.0.0', port=8080)