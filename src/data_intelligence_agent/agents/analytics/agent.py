from google.adk.code_executors import (
    VertexAiCodeExecutor
)
from google.adk.agents import Agent
from data_intelligence_agent.model import analytics_model
from data_intelligence_agent.agents.analytics.prompt import (
    return_instructions_analysis
)

analytics_agent = Agent(
    model=analytics_model,
    name="data_science_agent",
    instruction=return_instructions_analysis(),
    code_executor=VertexAiCodeExecutor(
        optimize_data_file=True,
        stateful=True,
    ),
)
