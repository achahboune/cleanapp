import pandas as pd

def clean_data(df):
    # Supprimer les lignes où le nom est vide
    df = df[df['Nom'].str.strip() != '']

    # Supprimer les lignes où la valeur n'est pas un nombre ou est inférieure ou égale à zéro
    df['Valeur'] = pd.to_numeric(df['Valeur'], errors='coerce')  # Convertir en numérique
    df = df[(df['Valeur'].notna()) & (df['Valeur'] > 0)]  # Garder uniquement les valeurs valides

    return df
