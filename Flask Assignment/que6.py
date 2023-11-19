# 6. Build a Flask app that allows users to upload files and display them on the website.

from flask import Flask , request , render_template,redirect
import os
app = Flask(__name__)

a = 'uploads'

@app.route("/")
def show_template():
    return render_template('image2.html')

@app.route('/upload',methods = ['post'])
def after_upload():
    file = request.files['file']
    if file == '':
        return redirect(request.url)

    if file:
        files = os.path.join(a,file.filename)
        file.save(files)
        return render_template('image2.html',filename = file.filename)



if __name__ == '__main__':
    app.run(debug = True)