import pandas as pd


def load_data(sht_url):
    csv_url = sht_url.replace("/edit#gif=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

#def push_data(sht_url):

