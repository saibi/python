from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '''
    <h1>Hello, World!!!</h1>
    <p>html contents</p>
    <a href="http://127.0.0.1:5000/user/saibi/18">dynamic url</a>
    '''

@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!!!'

if __name__ == "__main__":
    app.run()

