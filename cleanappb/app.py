import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
import gspread

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Initialiser l'application Flask
app = Flask(__name__)
CORS(app)  # Permettre les requêtes CORS de tous les domaines

# Récupérer le chemin du fichier de clés de service depuis les variables d'environnement
service_account_file = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")

# Définir les scopes pour l'API
scope = ['https://www.googleapis.com/auth/spreadsheets']

# Initialiser les credentials
creds = ServiceAccountCredentials.from_json_keyfile_name(service_account_file, scope)

# Initialiser le client Google Sheets
gc = gspread.authorize(creds)

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Ouvrir la feuille de calcul par son nom
        spreadsheet = gc.open("nom_de_votre_feuille")  # Remplacez par le nom de votre feuille
        worksheet = spreadsheet.sheet1  # Accéder à la première feuille

        # Récupérer toutes les données de la feuille
        data = worksheet.get_all_records()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/clean_data', methods=['POST'])
def clean_data():
    try:
        # Récupérer les données envoyées par la requête
        raw_data = request.json

        # Exemple de nettoyage de données
        cleaned_data = [entry for entry in raw_data if is_valid(entry)]
        
        return jsonify(cleaned_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def is_valid(entry):
    # Ajoutez ici votre logique de validation pour les données
    return True  # Placeholder : Modifiez selon vos besoins

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Écoute sur toutes les interfaces à port 5000
