from flask import Flask, request

app = Flask(__name__)

visitors = []

@app.route("/")
def index():
    return """
    <h1>Welcome to the pentest-server</h1>
    <ul>
    <li><a href=#>Test</a></li>
    <li><a href=#>Test2</a></li>
    </ul>
    """

@app.route("/hello/<name>")
def hello(name):
    visitors.append(name)
    return f"<h2>Hello {name}"

@app.route("/who")
def who():
    return f"<h3>Visitors: {', '.join(visitors)}"


@app.route('/submit', methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        text = request.form.get("text", "")
        return f"<h3>You sent {text}</h3>"
    return """
    <form method="POST">
        <input name="text">
        <button type="submit">Send</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)