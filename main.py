from flask import Flask, redirect,url_for

app = Flask(__name__)
@app.route('/')
def main():
    return "Welcome"
@app.route("/<place>")
def place(place):
    return f"<h1>Welcome {place}</h1>"
@app.route("/admin")
def admin():
    return redirect(url_for("place", place="admin"))

if __name__ == '__main__':
    app.run()