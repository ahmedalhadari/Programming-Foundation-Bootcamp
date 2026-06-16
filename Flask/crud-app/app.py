import sqlite3
from flask import Flask, redirect, request, render_template, url_for
app = Flask(__name__)
DATABASE = "students.db"

#DATABASE = r"D:\Hadari\Tuwaiq\Foundation Bootcamp - Programming Track\Python\Week 8\Flask\students.db"
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return redirect (url_for("students_list"))

@app.route("/students")
def students_list():
    conn = get_db()
    students = conn.execute(
        "SELECT * FROM students"
        ).fetchall()
    conn.close()
    return render_template("students_list.html", students=students)

@app.route("/students/add", methods=['POST', 'GET'])
def students_add():
    print (request.form["name"])
    return render_template("students_add.html")

if __name__ == "__main__":
    app.run(debug=True)