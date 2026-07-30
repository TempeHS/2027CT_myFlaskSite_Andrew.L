from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/gaming1")
def gamingweek1():
    return render_template("gaming1.html")


@app.route("/movie1")
def movieweek1():
    return render_template("movie1.html")


@app.route("/gaming2")
def gamingweek2():
    return render_template("gaming2.html")


@app.route("/movie2")
def movieweek2():
    return render_template("movie2.html")


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@app.route("/gamearticle1")
def gamearticle1():
    return render_template("gamearticle1.html")


@app.route("/gamearticle2")
def gamearticle2():
    return render_template("gamearticle2.html")


@app.route("/gamearticle3")
def gamearticle3():
    return render_template("gamearticle3.html")


@app.route("/gamearticle4")
def gamearticle4():
    return render_template("gamearticle4.html")


@app.route("/gamearticle5")
def gamearticle5():
    return render_template("gamearticle5.html")


@app.route("/gamearticle6")
def gamearticle6():
    return render_template("gamearticle6.html")


@app.route("/moviearticle1")
def moviearticle1():
    return render_template("moviearticle1.html")


@app.route("/moviearticle2")
def moviearticle2():
    return render_template("moviearticle2.html")


@app.route("/moviearticle3")
def moviearticle3():
    return render_template("moviearticle3.html")


@app.route("/moviearticle4")
def moviearticle4():
    return render_template("moviearticle4.html")


@app.route("/moviearticle5")
def moviearticle5():
    return render_template("moviearticle5.html")


@app.route("/moviearticle6")
def moviearticle6():
    return render_template("moviearticle6.html")


@app.route("/resultspage")
def resultspage():
    query = request.args.get("q", "").strip()
    return render_template("resultspage.html", query=query)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
