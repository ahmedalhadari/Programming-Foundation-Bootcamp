from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    x = 0 + 15
    return "<html><head> <title> This is Tuwaiq Academy </title> </head> <body> <h1> Hello Tuwaiq</h1> </body> </html>"


@app.route("/greet")
def greet():
    return "Hello, This is Greet Page "


@app.route("/dash")
def dashboard():
    return "This is dashboard Page "


if __name__ == "__main__":
    app.run(debug=True)

