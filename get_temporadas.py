import requests
import os
from dotenv import load_dotenv
import pandas as pd

# def get_times_df() -> pd.DataFrame:

load_dotenv()
api_key = os.getenv("API_KEY")

url = "http://api.football-data.org/v4/competitions/PL"

headers = {
    "X-Auth-Token": f"{api_key}"
}

response = requests.get(url,headers=headers)
data = response.json()

dados_tratados = []

for temporadas in data['seasons']:
        winner = temporadas['winner']

        id = temporadas['id']
        campeao = winner['name'] if winner else None
        inicio = temporadas['startDate']
        final = temporadas['endDate']

        dados_tratados.append({
            'id': id,
            'campeao': campeao,
            'inicio': inicio,
            'final': final
        })

df = pd.DataFrame(dados_tratados)
df_final = df.dropna(subset=['campeao'])
print(df_final)
    # return df