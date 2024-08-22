import importlib
import os
import sys
from typing import List
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import BaseTool

# Tools path
tools_dir = os.path.join(os.path.dirname(__file__), 'tools')
sys.path.append(tools_dir)


# Dinamically loads tools
def load_tools() -> List[BaseTool]:
    tools = [TavilySearchResults(max_results=2)]
    for filename in os.listdir(tools_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # Remove .py extension
            module = importlib.import_module(module_name)

            # Func
            if hasattr(module, module_name) and callable(getattr(module, module_name)):
                tools.append(getattr(module, module_name))
    return tools

