from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/templates/aboutus.html")
def aboutus():
    return render_template("aboutus.html")

@app.route("/templates/youtube_videos.html")
def youtubevideos():
    return render_template("youtube_videos.html")

@app.route("/templates/index.html")
def home2():
    return redirect(url_for("home"))

@app.route("/templates/links.html")
def links():
    return render_template("links.html")

if __name__ == "__main__":
    app.run()
