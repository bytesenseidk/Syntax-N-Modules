from flask import render_template, url_for, redirect, request, make_response
from main import app


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home Page")

@app.route("/backinbiz")
def testpage():
    return render_template("backinbiz.html", title="Second Test Page")

@app.route("/test")
def test():
    return render_template("test.html", title="Test Page")

@app.route("/useragent")
def agent():
    useragent = request.headers.get("User-Agent")
    return f"<p>Your Browser: {useragent}</p>"

@app.route("/cookie")
def cookie():
    response = make_response("<h1>This carries a cookie!</h1>")
    response.set_cookie("answer", "42")
    return response

@app.route("/editor")
def editor():
    return render_template("editor.html", title="Live Editor")
