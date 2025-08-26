import os

from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

from .tools import get_stock_price
from opik.integrations.adk import OpikTracer

import opik

# observability setup
opik.configure(
    api_key=os.getenv("OPIK_API_KEY"),
    workspace=os.getenv("OPIK_WORKSPACE"),
)
opik_tracer = OpikTracer()

# agent constructor
stock_agent = LlmAgent(
    name="stock_agent",
    model="gemini-2.5-pro",
    description=("An agent that provides stock market information"),
    instruction="""You are a helpful financial assistant that provides stock market information. 

When asked about stock prices:
1. Use the get_stock_price tool to retrieve current information
2. Always display the results in a clear, readable format
3. Include all important details: company name, current price, daily high/low, and currency
4. Format the response in a user-friendly way

Example response format:
**[Company Name] ([TICKER])**
- Current Price: $[price] [currency]
- Daily High: $[high]
- Daily Low: $[low]

Always acknowledge the tool results and present them clearly to the user.""",
    tools=[FunctionTool(get_stock_price)],
    before_agent_callback=opik_tracer.before_agent_callback,
    after_agent_callback=opik_tracer.after_agent_callback,
    before_model_callback=opik_tracer.before_model_callback,
    after_model_callback=opik_tracer.after_model_callback,
    before_tool_callback=opik_tracer.before_tool_callback,
    after_tool_callback=opik_tracer.after_tool_callback,
)
