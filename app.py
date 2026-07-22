from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/information")
def information():
    return render_template("information.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/articlefinder")
def articlefinder():
    return render_template("articlefinder.html")


@app.route("/gaming1")
def gaming1():
    return render_template("gaming1.html")


@app.route("/movie1")
def movie1():
    return render_template("movie1.html")


@app.route("/resultspage")
def resultspage():
    query = request.args.get("q", "").strip()
    return render_template("resultspage.html", query=query)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
