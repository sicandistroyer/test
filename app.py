print ("Hola Mundo")


@app.route('/')
def index():
    return render_template('index.html')

