from flask import Flask, redirect,url_for, render_template

app = Flask(__name__)
@app.route('/<Name>')
def main(Name):
    return render_template('index.html', name=Name)

if __name__ == '__main__':
    app.run(debug=True)