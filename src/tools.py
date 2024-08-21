from src.settings import cursor
import importlib


cursor.execute('SELECT * FROM tools')
tool_names = cursor.fetchall()
modules = []
for name in tool_names:
        try:
            module = importlib.import_module(f"tools.{name[1]}")  # nome[0] contiene il nome del modulo
            modules.append(module)
        except ModuleNotFoundError:
            print(f"Module '{name[1]}' not found!")

print(modules)
tools = modules


# web_search_tool = TavilySearchResults(k=3)