from google.cloud import bigquery
from oauth2client.client import GoogleCredentials
from oauth2client.service_account import ServiceAccountCredentials

def query_shakespeare(request, start_date, end_date):
    client = bigquery.Client.from_service_account_json('My Project-212bfbc62b78.json')
    print(start_date)
    query_params = [
        bigquery.ScalarQueryParameter(
            'start_date',
            'STRING',
            start_date
        ),
        bigquery.ScalarQueryParameter(
            'end_date',
            'STRING',
            end_date
        )
    ]
    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = query_params

    query_job = client.query(request, job_config=job_config)

    results = query_job.result()  # Waits for job to complete.
    return results