from flask import Flask, request, jsonify
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from clean_data import clean_data  # Importer la fonction de nettoyage

app = Flask(__name__)

# Configuration des autorisations pour accéder à Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\PC\\Desktop\\metabase\\meta.json', scope)
client = gspread.authorize(creds)

@app.route('/clean', methods=['POST'])
def clean_file():
    # Lire les données depuis Google Sheets
    spreadsheet = client.open_by_key('1HH3zfcxtCgZOaov2fN-ZQisAAA5giXuD9iKF8Gyd9Xw')
    worksheet = spreadsheet.sheet1
    data = worksheet.get_all_records()

    # Créer un DataFrame et nettoyer les données
    df = pd.DataFrame(data)
    cleaned_df = clean_data(df)

    # Exporter les résultats dans un fichier Excel
    output_file_path = 'C:\\Users\\PC\\Desktop\\metabase\\file1_cleaned.xlsx'
    cleaned_df.to_excel(output_file_path, index=False)

    return jsonify({"message": "Data cleaned successfully!", "file": output_file_path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
