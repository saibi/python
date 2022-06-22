from flask import Flask, request
from flask_restx import Api, Resource
from todo import Todo

app = Flask(__name__)
api = Api(
    app,
    version = '0.0.1',
    title = 'Title - rest api server',
    description = 'desc - hahahah',
    terms_url = '/',
    contact = "kimyoungmin@gmail.com",
    license = 'MIT'
)

api.add_namespace(Todo, '/todos')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")