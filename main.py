import requests
import os
from dotenv import load_dotenv
import pandas as pd
from get_times import get_times_df


if __name__ == "__main__":
    # Coleta
    df_times = get_times_df()

    # Imprime
    print(df_times)