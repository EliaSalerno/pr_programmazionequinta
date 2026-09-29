from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Cerca automaticamente il file dentro la cartella 'templates'
    return render_template('form.html')

if __name__ == '__main__':
    # host='0.0.0.0' permette l'accesso da smartphone e altri PC della rete locale
    app.run(host='0.0.0.0', port=5000, debug=True)
