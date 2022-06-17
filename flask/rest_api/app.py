# use rest api tester :  https://chrome.google.com/webstore/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm
# 
# GET test
#   method = GET
#   uri = http://127.0.0.1:5000/environments/hello
#
#   [SEND]
#   Response 로 200 OK json 으로된 language 를 받는다.
#
# POST test
#   method = POST
#   uri = http://127.0.0.1:5000/userLogin
#
#   HEADR
#       content-type : application/json
#   BODY
#       { "userName" : "saibi" }  
#
#   [SEND]
#   Response 로 전송한 json 그대로 받는다. 

from crypt import methods
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/userLogin', methods = ['POST'])
def userLogin():
    user = request.get_json()
    return jsonify(user)

@app.route('/environments/<language>')
def environments(language):
    return jsonify({"language":language})

if __name__ == "__main__":
    app.run()
