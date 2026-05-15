from data_intelligence_agent.tools.bigquery.client import get_client


def execute_sql(query: str):

    client = get_client()

    print("\nEXECUTING SQL:\n")
    print(query)

    query_job = client.query(query)

    rows = []

    for row in query_job.result():
        rows.append(dict(row.items()))

    return {
        "query": query,
        "rows": rows
    }