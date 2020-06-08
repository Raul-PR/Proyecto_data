from flask import Flask 
from flask import render_template 
from flask import request
from flask_MySQLdb import MySQL

app = Flask(__name__)
#conectal SQL a XAMPP
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcontacts'

mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

#agregar contactos
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
       fullname = request.form ['fullname']
       phone = request.form ['phone']
       email = request.form ['email']
       print(fullname)
       print(phone)
       print(email)
       return 'received'

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == "__main__":
    app.run(port=5000, debug=True)

