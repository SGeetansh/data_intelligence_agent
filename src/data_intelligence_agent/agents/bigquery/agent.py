from google.adk.agents import Agent
from google.adk.agents.callback_context import (
    CallbackContext
)

from data_intelligence_agent.agents.bigquery.prompts import (
    return_instructions_bigquery
)

from data_intelligence_agent.tools.bigquery.execute_sql import (
    execute_sql
)

from data_intelligence_agent.tools.bigquery.schema import (
    get_schema
)

from data_intelligence_agent.tools.bigquery.discovery import (
    list_datasets,
    list_tables
)

from data_intelligence_agent.tools.bigquery.session import (
    set_active_dataset
)

from data_intelligence_agent.model import db_model


def setup_before_agent_call(
    callback_context: CallbackContext
):

    active_dataset = callback_context.state.get(
        "active_dataset"
    )

    if active_dataset:

        schema = get_schema(active_dataset)

        callback_context.state["schema"] = schema


bigquery_agent = Agent(
    model=db_model,
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