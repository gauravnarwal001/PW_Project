from flask import Flask, request, render_template, redirect
import mysql.connector as c

app = Flask(__name__)

# Use context manager for database connection
with c.connect(host="localhost", user='root', password='gaurav123456') as mydb:
    db = mydb.cursor()

@app.route('/')
def show_template():
    return render_template("main_template.html")

@app.route('/database', methods=['POST'])
def database():
    return render_template("database.html")

@app.route('/create_database', methods=['GET', 'POST'])
def database_create_page():
    return render_template('create_database.html')

@app.route('/create_database/create', methods=['POST'])
def create_database():
    db_name = request.form.get('databasename')
    try:
        create_new_db = f'CREATE DATABASE {db_name}'
        db.execute(create_new_db)
        
        return redirect('/create_database?message=Database+Created+Successfully')

    except Exception as e:
        return redirect('/create_database?message=Database+Already+Exists')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port = 8000)
