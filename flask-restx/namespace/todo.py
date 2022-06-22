from flask import request
from flask_restx import Resource, Api, Namespace

todos = {}
count = 1

Todo = Namespace('Todo')

@Todo.route('')
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

@Todo.route('/<int:todo_id>')
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