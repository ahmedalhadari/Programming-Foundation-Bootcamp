from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/records")
def records():
    return render_template("records.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")


if __name__ == "__main__":
    app.run(debug=True)

