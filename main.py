from flask import Flask, redirect,url_for, render_template

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def home(): 
    return render_template('index.html')
@app.route('/Maths', methods=['GET','POST'])
def maths():
    return render_template('Maths.html') 
if __name__ == '__main__':
    app.run(debug=True)
