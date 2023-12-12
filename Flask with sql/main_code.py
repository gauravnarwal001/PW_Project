from flask import Flask, render_template, request
import mysql.connector as c

db_connection = c.connect(host = 'localhost',
                          user = 'root',
                          password = 'gaurav123456')

db = db_connection.cursor()

app = Flask(__name__)

@app.route('/')
def main_template():
    return render_template('main_template.html')

@app.route('/database',methods = ['post'])
def database_window():
    return render_template('database.html')

@app.route('/create_database',methods = ['post','get'])
def database_button():
    return render_template('create_database.html')

@app.route('/create_database/create',methods = ['post','get'])
def create_database():
    db_name = request.form.get('databasename')

    try:
        db_create = f'create database {db_name}'
        db.execute(db_create)
        return render_template('create_database.html',message = 'Database Created Successful', page = '/')
    except Exception as e:
        return render_template('create_database.html',message = 'Database Already Exist', page = '/create_database/create')
        



if __name__ == '__main__':
    app.run(host = '0.0.0.0')
