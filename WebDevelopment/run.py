from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/test")
def home():
    return render_template("Test.html", title="Test Page")

if __name__ == '__main__':
    app.run(debug=True)

