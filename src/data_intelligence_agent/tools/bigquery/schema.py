from data_intelligence_agent.tools.bigquery.client import get_client


def get_schema(dataset_id: str):
    """
    Retrieves the schema for all tables in a BigQuery dataset.

    Use this tool only when schema information is required
    for understanding the dataset or generating SQL queries.

    Do not call this tool unless a dataset has already
    been selected or explicitly provided.

    Args:
        dataset_id: The BigQuery dataset ID.

    Returns:
        A formatted text representation of all tables
        and their columns in the dataset.
    """

    client = get_client()

    tables = client.list_tables(dataset_id)

    schema_text = ""

    for table in tables:

        table_ref = client.get_table(table.reference)

        schema_text += f"\nTABLE: {table.table_id}\n"

        for field in table_ref.schema:
            schema_text += (
                f"- {field.name} ({field.field_type})\n"
            )

    print(schema_text)

    return schema_text