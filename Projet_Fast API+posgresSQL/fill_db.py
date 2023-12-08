from database import engine, SessionLocal
from models import EtablissementInfo
import pandas as pd
from sqlalchemy.orm import session

# Remplacez ceci par le chemin de votre fichier CSV
csv_file_path = 'C:/Users/briac/Documents/M2/Application of Big Data/etablissement_info.csv'

def load_data(csv_file_path):
    # Lire le fichier CSV dans un DataFrame
    df = pd.read_csv(csv_file_path,  sep=',', encoding='utf-8', header=0)

    df.to_sql('etablissement_info', engine, if_exists='append', index=False)

if __name__ == '__main__':
    load_data(csv_file_path)