import uuid
from datetime import datetime

from langchain_core.tools import tool, StructuredTool
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore, VectorStore
from langchain_openai import AzureOpenAIEmbeddings

from src.settings import llm


@tool
def create_tool(query: str, name: str):
    """Call to create a new Lang Graph tool.
    Has to be used ONLY if the user SPECIFICALLY asks to create a new Lang Graph tool

    Args:
        query: What the new Lang Graph tool should do.
        name: The name that the new tool will have (IN SNAKE CASE, WITHOUT SPACES OR SPECIAL CHARACTERS)
    """

    system = (f"Create a new Lang Graph tool that {query} using the following template."
              f"Replace the parts in caps with the code needed to make the tool work."
              f"Only return the working python code, DO NOT reply with any other type of text, not even before the code"
              f"Questions or long Strings MUST NOT be passed throught IF statements"
              f"Always import: 'from langchain_core.tools import tool'"
              f"DO NOT use Markdown, use simple text with the right indentation"
              f"DO NOT use ```python before the code")

    context = f"""
from langchain_core.tools import tool # KEEP THIS IMPORT
@tool # Do not change this line
# Tools have only one function, do not create other functions
def {name}(TOOL_PARAM: TOOL_PARAM_TYPE):
    # The tool description must be inside triple quotes, it must include the Parameters defined above.
    # This is an example of tool description for a chart creating tool:
    # Call to create a chart, given a list of numbers.
    # 
    # Args:
    #     numbers: A list of numbers
    "TOOL_DESCRIPTION"

    TOOL_CODE
    """
    code = llm.invoke([("system", system), ("human", context)])

    with open(f"tools/{name}.py", "w") as f:
        f.write(code.content)
        f.close()

    return {"messages": f"New tool {name} created"}
