# $ conda install pyopenssl
#
# create self-signed cert 
# $ openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
#
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!!!"

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))   