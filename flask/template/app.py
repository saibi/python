from flask import Flask, render_template

app = Flask(__name__)

student_data = {
    1: { "name": "superman", "score": { "korean": 90, "math":65 }},
    2: { "name": "batman", "score": { "korean": 75, "english": 80, "math":90 }}
}

@app.route('/')
def index():
    return render_template("index.html", template_student = student_data)

@app.route('/student/<int:id>')
def student(id):
    return render_template("student.html", template_name = student_data[id]["name"], template_score = student_data[id]["score"])

if __name__ == "__main__":
    app.run()