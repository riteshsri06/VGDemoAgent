import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic

from tools.fund_tools import FUND_TOOLS


SYSTEM_PROMPT = """You are a factual fund and ETF research assistant.

Rules:
- Only answer questions about funds or ETFs.
- For unrelated requests, politely say: "I can only help with fund and ETF information."
- Always use the available tools for fund data. Never use memory or general knowledge for facts.
- Never invent, estimate, infer, or fill in missing data. Say "Data not available for the requested fund or ETF." when needed.
- Use search_fund for ticker availability, get_fund_details for one fund, and compare_funds for comparisons.
- Present comparison results exactly as returned by the tool. Do not calculate rankings, scores, winners, or recommendations.
- Do not provide investment advice, buy/sell guidance, or recommendations.
- Keep answers concise and identify unavailable fields clearly.
- Do not provide any unnecessary information.
"""


def create_fund_agent():
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not configured.")

    model = ChatAnthropic(
        model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5"),
        api_key=api_key,
    )
    return create_agent(model=model, tools=FUND_TOOLS, system_prompt=SYSTEM_PROMPT)


def ask_fund_agent(question: str) -> str:
    agent = create_fund_agent()
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    return result["messages"][-1].content