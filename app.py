from flask import Flask 
from flask import render_template


app = Flask(__name__, template_folder='templates') # Creo la instancia de Flask

@app.route('/') #defino una ruta
def index(): #Defino la funcion de blque de codigo
    return render_template('/html/index.html') #retorno el template

if __name__ == '__main__':
    app.run(debug=True) 


