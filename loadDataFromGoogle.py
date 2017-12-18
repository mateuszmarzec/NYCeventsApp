from google.cloud import bigquery
from oauth2client.client import GoogleCredentials
from oauth2client.service_account import ServiceAccountCredentials

def query_shakespeare(request):
    client = bigquery.Client.from_service_account_json('My Project-212bfbc62b78.json')
    query_job = client.query(request)

    results = query_job.result()  # Waits for job to complete.
    return results