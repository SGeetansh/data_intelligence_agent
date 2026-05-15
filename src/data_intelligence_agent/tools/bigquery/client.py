from google.cloud import bigquery

client = bigquery.Client()

def get_client():
    return client