##4. Create a Flask app with a form that accepts user input and displays it.

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def template():
    return render_template("name.html")

@app.route('/submit',methods = ['post'])
def full_name():
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    return f'{first_name} {last_name}'

app.run(host='0.0.0.0')