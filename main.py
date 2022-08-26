from pathlib import Path
from flask import Flask, render_template, request
from pytube import YouTube


app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def home():
    if request.method == "GET":
        return render_template("home.html")

    if request.method == "POST":
        url = request.form["url"]
        path = str(Path.home() / "Downloads")

        #TODO find a way to implement loading symbold when awaiting download
        # loading = True
        # return render_template("home.html", loading=loading)

        try:
            contents = YouTube(url)
            contents.streams.get_highest_resolution().download(path)

            title = contents.title

            downloaded = True
            return render_template("home.html", title=title, downloaded=downloaded)
        except:
            failed = True
            return render_template("home.html", failed=failed)


if __name__ == "__main__":
    app.run(debug=True)
