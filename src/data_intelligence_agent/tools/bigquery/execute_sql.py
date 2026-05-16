from data_intelligence_agent.tools.bigquery.client import get_client


def execute_sql(query: str):
    """
    Executes a BigQuery SQL query and returns the results.

    Use this tool only after generating a valid SQL query.

    Rules:
    - Only execute SELECT queries
    - Never execute DELETE, DROP, UPDATE, INSERT, or ALTER queries
    - Only use tables and columns confirmed through schema inspection
    - Prefer limiting results to a reasonable number of rows

    Args:
        query: A valid BigQuery SQL query.

    Returns:
        A dictionary containing:
        - the executed SQL query
        - the returned rows as JSON-compatible objects
    """

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