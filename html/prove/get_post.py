from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form2.html')

@app.route('/risultato_get', methods=['GET'])
def risultato_get():
    dati = request.args          # dati presi dall'URL
    return render_template('risultato.html',
                           metodo='GET',
                           dati=dati,
                           url=request.url)

@app.route('/risultato_post', methods=['POST'])
def risultato_post():
    dati = request.form          # dati presi dal corpo della richiesta
    return render_template('risultato.html',
                           metodo='POST',
                           dati=dati,
                           url=request.url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
