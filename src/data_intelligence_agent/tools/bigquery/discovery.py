from data_intelligence_agent.tools.bigquery.client import get_client
from google.adk.tools import ToolContext

def list_datasets():
    """
    Lists available datasets the user can choose from.

    This tool does not select a dataset.
    """

    client = get_client()

    datasets = client.list_datasets()

    output = []

    for dataset in datasets:
        output.append(dataset.dataset_id)

    print("\nDATASETS:")
    print(output)

    return output

def list_tables(tool_context: ToolContext):
    """
    Lists tables in the currently active dataset.

    Use this tool only after a dataset has been
    explicitly selected by the user.

    This tool reads the active dataset from
    session state.

    Do not call this tool if no active dataset
    is selected.

    Returns:
        A list of table names in the active dataset.
    """
    dataset_id = tool_context.state.get("active_dataset")
    if not dataset_id:
        return {
            "status": "error",
            "message": "No active dataset selected."
        }
    client = get_client()

    tables = client.list_tables(dataset_id)

    output = []

    for table in tables:
        output.append(table.table_id)

    return output