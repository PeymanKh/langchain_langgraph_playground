"""
This modules only add tools to the llm. to pass the tool back to the llm, check react-agent
implementation.
"""
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from config.config import config


#################### Method 1: Simple ####################
# Create LLM instance
llm = ChatOpenAI(
    model=config.openai_model,
    api_key=config.openai_api_key
)

# Define the function
def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

# Bind the tool
llm = llm.bind_tools([multiply])

# Invoke
tool_call = llm.invoke([HumanMessage(content=f"What is 2 multiplied by 3", name="Peyman")])
print(tool_call)

#################### Method 2: Structured tool (good for async) ####################
from langchain_core.tools import StructuredTool

# Create LLM instance
llm2 = ChatOpenAI(
    model=config.openai_model,
    api_key=config.openai_api_key
)

# Define the function
def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

# Create the tool from the function
multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description="Multiplies two integers."
)

# Bind the tool
llm_with_tools = llm2.bind_tools([multiply_tool])

# Invoke
response = llm_with_tools.invoke("What is 5 times 6?")
print(response.tool_calls)

#################### Method 2: Most Customizable ####################
"""This method allows for error handling in _run, etc..."""
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

# Define schema for tool inputs (optional but recommended)
class MultiplyInput(BaseModel):
    a: int = Field(description="First integer")
    b: int = Field(description="Second integer")

# Subclass BaseTool
class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiplies two integers."
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b

# Instantiate the tool
multiply_tool = MultiplyTool()

# Create LLM instance
llm3 = ChatOpenAI(
    model=config.openai_model,
    api_key=config.openai_api_key
)

llm_with_tools = llm3.bind_tools([multiply_tool])

# Invoke
response = llm_with_tools.invoke("What is 7 times 8?")
print(response.tool_calls)

