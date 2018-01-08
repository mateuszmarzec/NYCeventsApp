from google.cloud import bigquery


def query_shakespeare(request, start_date, end_date, coordinates):
    client = bigquery.Client.from_service_account_json('My Project-212bfbc62b78.json')
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
        ),
        bigquery.ScalarQueryParameter(
            'lat',
            'FLOAT',
            coordinates['latitude']
        ),
        bigquery.ScalarQueryParameter(
            'lng',
            'FLOAT',
            coordinates['longitude']
        ),
    ]
    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = query_params

    query_job = client.query(request, job_config=job_config)

    results = query_job.result()  # Waits for job to complete.
    return results