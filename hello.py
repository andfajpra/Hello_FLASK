from flask import Flask #Flask con F mayuscula es una app es una clase

app= Flask(__name__) #nos creamos la aplicación

#--Utilizamos un decorador de app (es una funcion de python que a la funcion q nosotros vamos a crear abajo la va a hacer accesible desde el servidor)
@app.route("/hola")  #decorador que abre puerta entre servidor y python
def primeraentrada():
    return "Hola, mundo"

@app.route("/adios")
def salida():
    return "Hasta luego, Mari Carmen!!!"


@app.route("/doble/<numero>")
def doble(numero):
    return str(numero*2)
