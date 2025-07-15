from langchain_community.llms import FakeListLLM
from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
from openai import APIError, APIConnectionError, RateLimitError, AuthenticationError

from config.config import config


#################### OpenAI ####################
openai_llm = ChatOpenAI(
    model=config.openai_model,
    api_key=config.openai_api_key.get_secret_value(),
    temperature=config.openai_temperature,
    max_tokens=config.openai_max_tokens,
    top_p=config.openai_top_p,
    max_retries=3,
)

#################### Gemini ####################
# google_llm = ChatGoogleGenerativeAI(
#     model=config.google_model,
#     top_p=config.google_top_p,
#     temperature=config.google_temperature,
#     max_tokens=config.google_max_tokens,
#     api_key=config.google_api_key.get_secret_value(),
# )

#################### Development test LLM ####################
fake_llm = FakeListLLM(responses=["hello!"])


#################### Error Handling ####################
try:
    response = openai_llm.invoke("Who am I talking to?")
    print(response.content)
    # Process the response
except AuthenticationError as e:
    print(f"Invalid API key: {e}")  # Handle wrong API key
except RateLimitError as e:
    print(f"Rate limit or quota issue: {e}")  # Could indicate balance problems
except APIConnectionError as e:
    print(f"Connection error: {e}")  # Network or server issues
except APIError as e:
    print(f"General OpenAI API error: {e}")
    print(f"Output parsing failed: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")


