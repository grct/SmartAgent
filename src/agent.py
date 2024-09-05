from typing import Annotated

from langgraph.constants import START
from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from src.tools import load_tools
from settings import llm


class State(TypedDict):
    messages: Annotated[list, add_messages]
    selected_tools: list[str]


graph_builder = StateGraph(State)
tools = load_tools()


def chatbot(state: State):
    selected_tools = load_tools()
    llm_with_tools = llm.bind_tools(selected_tools)
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


def load_new_tools(state: State):
    updated_tools = load_tools()
    return {'selected_tools': updated_tools}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("load_new_tools", load_new_tools)

tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

graph_builder.add_edge("tools", "load_new_tools")
graph_builder.add_edge("load_new_tools", "chatbot")
graph_builder.set_entry_point("chatbot")
graph = graph_builder.compile()

while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in graph.stream({"messages": ("user", user_input)}):
        for value in event.values():
            try:
                print("Assistant:", value["messages"][-1].content)
            except:
                pass
