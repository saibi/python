# use api tester
# POST
#   http://127.0.0.1:5000/todos
#   HEADER
#       content-type : application/json
#   BODY
#       { "data" : "saibi" }
#
# GET
#   http://127.0.0.1:5000/todos/1
# 
# PUT
#   http://127.0.0.1:5000/todos/1
#   HEADER
#       content-type : application/json
#   BODY
#       { "data" : "saibi-new" }  
#
# DELETE
#   http://127.0.0.1:5000/todos/1



from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

todos = {}
count = 1

@api.route('/todos')
class TodoPost(Resource):
    def post(self):
        global count
        global todos 

        idx = count
        count += 1
        todos[idx] = request.json.get('data')
        print(todos[idx])
        print(todos)
        return {
            'todo_id': idx,
            'data': todos[idx]
        }

@api.route('/todos/<int:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        print(todos[todo_id])
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }

    def put(self, todo_id):
        todos[todo_id] = request.json.get('data')
        print(todos[todo_id])
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }

    def delete(self, todo_id):
        print('delete:', todos[todo_id])
        del todos[todo_id]
        print(todos)
        return {
            "delete": "success"
        }
        
if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = "5000")
