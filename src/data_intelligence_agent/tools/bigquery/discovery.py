from data_intelligence_agent.tools.bigquery.client import get_client


def list_datasets():

    client = get_client()

    datasets = client.list_datasets()

    output = []

    for dataset in datasets:
        output.append(dataset.dataset_id)

    print("\nDATASETS:")
    print(output)

    return output

def list_tables(dataset_id: str):

    client = get_client()

    tables = client.list_tables(dataset_id)

    output = []

    for table in tables:
        output.append(table.table_id)

    print(f"\nTABLES IN {dataset_id}:")
    print(output)

    return output