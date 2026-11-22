import requests
import os
from dotenv import load_dotenv
import pandas as pd

def get_times_df() -> pd.DataFrame:

    load_dotenv()
    api_key = os.getenv("API_KEY")

    url = "http://api.football-data.org/v4/competitions/PL/teams"

    headers = {
        "X-Auth-Token": f"{api_key}"
    }

    response = requests.get(url,headers=headers)
    data = response.json()

    dados_tratados = []

    for time in data['teams']:
        id = time['id']
        nome = time['name']
        nome_abreviado = time['shortName']
        sigla = time['tla']
        fundacao = time['founded']
        cores = time['clubColors']
        estadio = time['venue']

        dados_tratados.append({
            'id': id,
            'Nome': nome,
            'Nome Abreviado': nome_abreviado,
            'Sigla': sigla,
            'Fundação': fundacao,
            'Cores': cores,
            'Estádio': estadio
        })

    df = pd.DataFrame(dados_tratados)
    return df