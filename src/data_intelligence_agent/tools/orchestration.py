from google.adk.tools import ToolContext
from google.adk.tools.agent_tool import AgentTool

from data_intelligence_agent.agents.bigquery.agent import (
    bigquery_agent
)

from data_intelligence_agent.agents.analytics.agent import (
    analytics_agent
)


async def call_bigquery_agent(
    question: str,
    tool_context: ToolContext,
):
    """
    Calls the BigQuery agent to retrieve data.
    """

    agent_tool = AgentTool(
        agent=bigquery_agent
    )

    result = await agent_tool.run_async(
        args={"request": question},
        tool_context=tool_context,
    )

    tool_context.state["db_agent_output"] = result

    return result


async def call_analytics_agent(
    question: str,
    tool_context: ToolContext,
):
    """
    Calls the analytics agent to analyze retrieved data.
    """

    db_output = tool_context.state.get(
        "db_agent_output"
    )

    question_with_data = f"""
Question:
{question}

Retrieved data:
{db_output}
"""

    agent_tool = AgentTool(
        agent=analytics_agent
    )

    result = await agent_tool.run_async(
        args={
            "request": question_with_data
        },
        tool_context=tool_context,
    )

    return result