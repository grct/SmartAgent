from langchain_anthropic import ChatAnthropic
from langchain_openai import AzureChatOpenAI

# llm = ChatAnthropic(model="claude-3-haiku-20240307")
llm = AzureChatOpenAI(
    azure_deployment="gpt-4",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)