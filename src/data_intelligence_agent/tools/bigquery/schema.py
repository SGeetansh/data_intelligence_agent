from data_intelligence_agent.tools.bigquery.client import get_client


def get_schema(dataset_id: str):

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