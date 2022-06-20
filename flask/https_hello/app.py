# $ conda install pyopenssl
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!!!"

if __name__ == "__main__":
    app.run(ssl_context='adhoc')    