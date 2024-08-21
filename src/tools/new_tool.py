import uuid
from datetime import datetime

from langchain_core.tools import tool
from src.settings import llm, cursor, conn

@tool
def new_tool(query: str, name: str):
    """Call to create a new Lang Graph tool.
    Has to be used ONLY if the user SPECIFICALLY asks to create a new Lang Graph tool

    Args:
        query: What the new Lang Graph tool should do.
        name: The name that the new tool will have (WITHOUT SPACES OR SPECIAL CHARACTERS)
    """

    system = (f"Create a new Lang Graph tool that {query} using the following template."
              f"Replace the parts in caps with the code needed to make the tool work."
              f"Only return the working python code, DO NOT reply with any other type of text, not even before the code"
              f"DO NOT use markdown, use simple text with the right indentation")

    context = """
    from langchain_core.tools import tool
    @tool
    def TOOL_NAME(TOOL_PARAM: TOOL_PARAM_TYPE):
        # The tool description must be inside triple quotes
        "TOOL_DESCRIPTION"

        TOOL_CODE
    """
    code = llm.invoke([("system", system), ("human", context)])

    f = open(f"{name}.py", "w")
    f.write(code.content)
    f.close()

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO tools (id, nome, data_creazione)
        VALUES (?, ?, ?)
    ''', (str(uuid.uuid4()), name, now))
    conn.commit()


    return "Done"