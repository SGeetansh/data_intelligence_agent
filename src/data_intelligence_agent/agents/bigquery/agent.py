from google.adk.agents import Agent
from google.adk.agents.callback_context import (
    CallbackContext
)
from data_intelligence_agent.agents.bigquery.prompts import (
    return_instructions_bigquery
)
from data_intelligence_agent.tools.bigquery.execute_sql import execute_sql
from data_intelligence_agent.tools.bigquery.schema import get_schema
from data_intelligence_agent.tools.bigquery.discovery import list_datasets, list_tables
from data_intelligence_agent.tools.bigquery.session import (
    set_active_dataset
)
from data_intelligence_agent.model import model

def setup_before_agent_call(
    callback_context: CallbackContext
):

    active_dataset = callback_context.state.get(
        "active_dataset"
    )

    base_instruction = (
        return_instructions_bigquery()
    )

    if active_dataset:

        schema = get_schema(active_dataset)

        callback_context.state["schema"] = schema

        callback_context._invocation_context.agent.instruction = ( # type: ignore
            base_instruction
            + f"""

ACTIVE DATASET:
{active_dataset}

DATABASE SCHEMA:
{schema}

Use this schema for SQL generation.
"""
        )

    else:

        callback_context._invocation_context.agent.instruction = ( # type: ignore
            base_instruction
            + """

No active dataset is currently selected.

Use:
- list_datasets
- set_active_dataset

before attempting SQL queries.
"""
        )

bigquery_agent = Agent(
    model=model,
    name="bigquery_agent",
    instruction=return_instructions_bigquery(),
    before_agent_callback=setup_before_agent_call,
    tools=[
        list_datasets,
        list_tables,
        get_schema,
        set_active_dataset,
        execute_sql,
    ]
)