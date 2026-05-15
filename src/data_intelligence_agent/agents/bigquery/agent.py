from google.adk.agents import Agent
from data_intelligence_agent.agents.bigquery.prompts import (
    return_instructions_bigquery
)
from data_intelligence_agent.tools.bigquery.execute_sql import execute_sql
from data_intelligence_agent.tools.bigquery.schema import get_schema
from data_intelligence_agent.tools.bigquery.discovery import list_datasets, list_tables

from data_intelligence_agent.model import model

bigquery_agent = Agent(
    model=model,
    name="bigquery_agent",
    instruction=return_instructions_bigquery(),
    tools=[
    list_datasets,
    list_tables,
    get_schema,
    execute_sql,
    ]
)