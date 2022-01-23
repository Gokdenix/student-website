from flask import Flask

app = Flask(__name__)

@app.route("/<place>")
def home(place):
    return "<h1>Welcome {place}</h1>"

if __name__ == '__main__':
    app.run()