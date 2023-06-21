from flask import Flask , request #Obtener datos de formulario
from flask import render_template
from flaskext.mysql import  MySQL

app = Flask(__name__, template_folder='templates') # Creo la instancia de Flask

mysql = MySQL()#Instancia de la clase MYSQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # Defino el host
app.config['MYSQL_DATABASE_PORT'] = 3306 # Defino el puerto
app.config['MYSQL_DATABASE_USER'] = 'root' # Defino el usuario
app.config['MYSQL_DATABASE_PASSWORD'] = '' # Defino la contraseña
app.config['MYSQL_DATABASE_DB'] = 'movies' # Defino la base de datos
mysql.init_app(app) # Inicializo la aplicación



@app.route('/') #defino una ruta
def index(): #Defino la funcion de blque de codigo
    sql = "SELECT * FROM movies.movies;" # Defino la consulta

    conn = mysql.connect() # Creo la conexión
    cursor = conn.cursor() # Creo el cursor
    cursor.execute(sql) # Ejecuto la consulta

    data_movies = cursor.fetchall() # Obtengo los datos

    cursor.close() # Cierro el curso 
    return render_template('/html/index.html') #retorno el template

if __name__ == '__main__':
    app.run(debug=True) #ejecuto el servidor en el puerto 8000

@app.route('/create')
def create(): #f funciion para renderizar el template de crear peliculas
    return render_template('/create.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000) # Ejecutamos el servidor 8000


@app.route('/store', methods=['POST']) # Creamos la ruta para almacenar peliculas
def store(): # Funcion para almacenar peliculas
    title = request.form['title'] #Obtenemos el titulo
    lenght = request.form['longitud']

if __name__ == '__main__': 
    app.run(debug=True, port=8000)#  Ejecutamos el servidor en el puerto 8000




