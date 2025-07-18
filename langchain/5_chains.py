"""
Chains implementation guide.
"""

from langchain_openai import ChatOpenAI

from config.config import config


#################### 1. Basic Chain ####################
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Create LLM instance
llm = ChatOpenAI(
    model=config.openai_model,
    api_key=config.openai_api_key
)

# Define a chat-style prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Explain {topic} in simple terms.")
])

# Compose the chain using pipes
basic_chain = prompt | llm | StrOutputParser()

# Invoke with input
response = basic_chain.invoke({"topic": "GPU"})
print(response)


#################### 2. Transformation & Custom logic ####################
"""
Transformations help chains process beyond raw LLM outputs
"""
# Compose the chain using pipes
transformed_chain = basic_chain | (lambda x: x.upper())

# Invoke with input
response = transformed_chain.invoke({"topic": "GPU"})
print(response)

############# RunnableLambda #############
from langchain_core.runnables import RunnableLambda
# Define a custom function
def word_count(text: str) -> str:
    """Returns the word count of the text."""
    return f"Word count: {len(text.split())}"

# Wrap and add to chain
custom_chain = basic_chain | RunnableLambda(word_count)

# Invoke
response = custom_chain.invoke({"topic": "GPU"})
print(response)
