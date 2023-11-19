from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def navigation():
    return render_template('form.html')

@app.route('/submit',methods = ['post'])
def output():
    return ' Thanks for sign in'

app.run(host='0.0.0.0')