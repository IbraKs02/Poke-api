from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Paramètres de connexion à la base de données PostgreSQL sur Render
DB_HOST = "dpg-cvq353bipnbc73cil1og-a.frankfurt-postgres.render.com"
DB_NAME = "pokefeuille_sql_base"
DB_USER = "pokefeuille_sql_base_user"
DB_PASSWORD = "rm0IWPFUkWbFi8OQdU6d6LrHD7pKwDJx"

# Connexion à la base de données PostgreSQL
def connect_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        sslmode='require'
    )
    return conn

# Route pour récupérer les données depuis la base PostgreSQL
@app.route('/api/cartes', methods=['GET'])
def get_cartes():
    conn = connect_db()
    cur = conn.cursor()

    # Exécuter une requête SQL pour récupérer les données des cartes
    cur.execute("SELECT * FROM cartes_details_fr")
    rows = cur.fetchall()

    # Fermer la connexion à la base de données
    cur.close()
    conn.close()

    # Retourner les résultats sous forme de JSON
    return jsonify(rows)

if __name__ == "__main__":
    # Écouter sur l'adresse 0.0.0.0 et le port dynamique
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
