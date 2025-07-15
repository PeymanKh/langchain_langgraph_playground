from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

############### Method 1 ###############
python_developer_prompt = PromptTemplate.from_template(
    "You are professional python developer. answer this question: {question}"
)

prompt1 = python_developer_prompt.invoke({'question': 'what is cpu?'})
prompt2 = python_developer_prompt.format_prompt(question='what is cpu?')
print(prompt1)
print(prompt2)

############### Method 2 ###############
python_developer_prompt = ChatPromptTemplate(
    [
        ("system", "You are professional python developer."),
        ("user", "{user_query}")
    ]
)

prompt3 = python_developer_prompt.invoke({'user_query': 'what is cpu?'})  # Returns: messages=[...]
prompt4 = python_developer_prompt.format_messages(user_query='what is cpu?')  # Returns list: [...]
print(prompt3)
print(prompt4)

