from google.adk.tools import ToolContext

from data_intelligence_agent.tools.bigquery.discovery import (
    list_datasets
)


def set_active_dataset(
    dataset_id: str,
    tool_context: ToolContext
):
    """
    Sets the active dataset for future queries.

    Only call this tool after the user has explicitly
    selected a dataset.

    Never automatically choose a dataset on behalf
    of the user.
    """

    datasets = list_datasets()

    if dataset_id not in datasets:
        return {
            "status": "error",
            "message": (
                f"Dataset '{dataset_id}' not found."
            )
        }

    tool_context.state["active_dataset"] = dataset_id

    return {
        "status": "success",
        "active_dataset": dataset_id
    }