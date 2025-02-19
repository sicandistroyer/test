print ("Hola Mundo")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alumnos')
def index():
    return render_template('alumnos.html')


test
