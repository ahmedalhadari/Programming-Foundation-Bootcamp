import sqlite3
from flask import Flask, redirect, request, render_template, url_for
app = Flask(__name__)
DATABASE = "students.db"

# DATABASE = r"D:\Hadari\Tuwaiq\Foundation Bootcamp - Programming Track\Python\Week 8\Flask\students.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    return redirect(url_for("students_list"))


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
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        city = request.form["city"]
        age = request.form["age"]
        gpa = request.form["gpa"]

        conn = get_db()
        conn.execute(
            """
            INSERT INTO students (name, email, city, age, gpa)
            VALUES (?, ?, ?, ?, ?)
            """, (name, email, city, age, gpa)
        )
        conn.commit()
        conn.close()
    return render_template("students_add.html")


@app.route("/students/delete/<int:student_id>")
def students_delete(student_id):

    conn = get_db()
    conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("students_list"))


@app.route("/students/edit/<int:student_id>", methods=["GET", "POST"])
def students_edit(student_id):


    if request.method == "POST":
        #Update Statement
        name = request.form["name"]
        email = request.form["email"]
        city = request.form["city"]
        age = request.form["age"]
        gpa = request.form["gpa"]
        
        conn = get_db()
        conn.execute("""
                     UPDATE students SET name=?,
                     email=?, city=?, age=?, gpa=?
                     WHERE id=? """, (name, email, city, age, gpa, student_id))
        conn.commit()
        conn.close()
    conn = get_db()   
    student = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
    conn.close()
    return render_template("students_edit.html", student=student)
        

if __name__ == "__main__":
    app.run(debug=True)
