from flask import Flask, jsonify
import mysql.connector

user="root"
password="Password123!"
host="xxx.xxx.xxx.xxx"
port=3306
database="muscolin"

app = Flask(__name__)

@app.route('/corsi')
def elencoCorsi():
    connessione = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database
        )

    cursore=connessione.cursor(dictionary=True)
    cursore.execute("SELECT * FROM corsi")
    risultato=cursore.fetchall()
    cursore.close()
    connessione.close()

    risposta=jsonify(risultato)
    risposta.headers.add("Access-Control-Allow-Origin", "*")
    return(risposta)
