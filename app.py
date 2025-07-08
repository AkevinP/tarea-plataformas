#Importar herramienta FLASK
from flask import Flask, request 

#"Servidor local"
app = Flask(__name__)

#End point y el metodo GET
@app.route('/usuarios/api/v1/saludo', methods=['GET']) 

#Función
def saludo():
    user_id = request.args.get('id') #Verificación del id
    if user_id:
        return f"El id del usuario es {user_id}" #Con parametros
    else:
        return "Lista de todos los usuarios." #Sin parametros

if __name__ == '__main__': #Servidor se ejecute correctamente
    app.run(debug=True)
