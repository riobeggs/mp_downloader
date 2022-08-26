from pytube import YouTube
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def home():
    if request.method == "GET":
        return render_template("home.html")

    if request.method == "POST":
        try:
            print("success")
        except:
            failed = True
            return render_template("home.html", failed=failed)


if __name__ == "__main__":
    app.run(debug=True)
