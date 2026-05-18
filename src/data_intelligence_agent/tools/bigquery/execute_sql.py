from data_intelligence_agent.tools.bigquery.client import (
    get_client
)

MAX_ROWS = 20


def execute_sql(query: str):
    """
    Executes a safe BigQuery SQL query.

    This tool is intended for:
    - simple database questions
    - previews
    - lightweight aggregations

    Heavy analytics and large-scale dataframe
    analysis should be handled by the analytics
    agent using Vertex Code Executor.

    Rules:
    - Only SELECT queries allowed
    - Destructive queries are forbidden
    - Raw retrieval queries are automatically limited

    Args:
        query:
            Valid BigQuery SQL query.

    Returns:
        Dictionary containing:
        - executed query
        - returned rows
        - row count
    """

    client = get_client()

    query = query.strip().rstrip(";")

    lowered = query.lower()

    forbidden_keywords = [
        "delete",
        "update",
        "insert",
        "drop",
        "alter",
        "truncate",
        "create",
        "merge",
    ]

    if any(word in lowered for word in forbidden_keywords):
        raise ValueError(
            "Only read-only SELECT queries are allowed."
        )

    analytical_keywords = [
        "group by",
        "count(",
        "avg(",
        "sum(",
        "min(",
        "max(",
        "having",
        "over(",
    ]

    is_analytical_query = any(
        keyword in lowered
        for keyword in analytical_keywords
    )

    # Limit only raw retrieval queries
    if (
        not is_analytical_query
        and "limit" not in lowered
    ):
        query += f" LIMIT {MAX_ROWS}"

    print("\nEXECUTING SQL:\n")
    print(query)

    query_job = client.query(query)

    rows = [
        dict(row.items())
        for row in query_job.result()
    ]

    return {
        "query": query,
        "row_count": len(rows),
        "rows": rows,
    }