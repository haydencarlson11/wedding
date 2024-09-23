from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == 'GET':
        return render_template("survey.html")
    process_form(request.form)
    return render_template("thanks.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/login")
def info():
    return render_template("login.html")

app.route("/thanks")
def thanks():
    return render_template("thanks.html")

app.route("/responses")
def responses():
    return render_template("responses.html")


def process_form(response):
    print(response)
    for key, val in response.items():
        print(f'{key} {val}')