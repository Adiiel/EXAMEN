from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/default', defaults={'nombre' : 'Pretty Printed'})
@app.route('/default/<nombre>')
def default(nombre):
    return 'El valor es: ' + nombre


#tipos de rutas
@app.route('/stringroute/<string:nombre>')
def stringroute(nombre):
    if type(nombre):
        string = "string"
    return 'El string es: ' + nombre + "y es un tipo de dato:  " + string

@app.route('/introute/<int:edad>')
def introute(edad):
    #return 'El entero (edad) es: ' + str(edad)
    return 'El entero (edad) es: %d ' % edad

@app.route('/floatroute/<float:peso>')
def floatroute(peso):
    return 'El flotante (peso) es: ' + str(peso)

@app.route('/pathroute/<path:miruta>')
def pathroute(miruta):
    return 'La ruta es: ' + miruta

@app.route('/conbinedroute/<string:mystring>/<int:myint>')
def combinedroute(mystring, myint):
    return 'El valor string es: %s , y el valor entero es %d ' %(mystring, myint)

@app.route('/urls/<string:nombrefuncion>')
def url(nombrefuncion):
    #a = nombrefuncion
    #return '<h1>' + url_for(a) + '</h1>'

    return '<h1>' + url_for('floatroute', peso=15.5, _external=True) + '</h1>'
#Otro ejemplo para usar url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next="/"))
    print(url_for('profile', username='Abel Huanca'))

    print("-------------------")

    print(index)

if __name__ == "__main__":
    app.run(debug=True)
