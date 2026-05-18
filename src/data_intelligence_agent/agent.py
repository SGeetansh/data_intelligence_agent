from google.adk.agents import Agent

from data_intelligence_agent.model import orchestrator_model

from data_intelligence_agent.tools.orchestration import (
    call_bigquery_agent,
    call_analytics_agent,
)

from data_intelligence_agent.root_prompt import (
    return_root_instructions
)

root_agent = Agent(
    model=orchestrator_model,
    name="root_agent",
    instruction=return_root_instructions(),
    tools=[
        call_bigquery_agent,
        call_analytics_agent,
    ]
)