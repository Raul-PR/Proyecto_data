from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
#Parametros, por ejemplo enviar una Query a una base de datos de un usuario

#@app.route('/user/<userid>')
#def get_user(userid):
 #   return userid

#Ejecutar una petición con enteros y pasarlo a un String

@app.route('/user/<int:userid>')
def get_user(userid):
    return 'Integrer %d' % userid


@app.route('/user/<int:userid>', methods=['GET'])
def get_user(userid):
    return 'Integrer %d' % userid




