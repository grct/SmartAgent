# Smart Agent with LangGraph

This project uses **[LangGraph](https://langchain-ai.github.io/langgraph/)**, a library for building stateful, multi-actor applications with LLMs.

The goal is to develop an agent capable of autonomously generating the necessary tools to fulfill user requests.
This is a single-agent application, where the only initially available tools for the agent are `create_tool` and `Tavily` for web search.


The application consists of three main nodes:
-   **Chatbot**: Facilitates conversation between the human and the AI.
-   **Tools** (with individual nodes for each tool): Represents the tools available to the AI to fulfill the user's request.
-   **load_new_tools**: Reloads the tools each time a new one is created.


This is the current graph:
![graph](https://i.imgur.com/beZdYA7.png)

# Demonstration
In this example, I make a request to the agent that requires 3 steps:

1.  Find the price of a **Tesla Model 3**.
2.  Find the price of a **Camel**.
3.  Create a **Tool** that, given the input of a number of Camels, calculates how many more are needed to buy a Tesla Model 3.

This is the query:

> Find the current price of a Tesla Model 3 and a camel. Then create a
> tool that, given as input a number of camels, tells me how many are
> missing to buy a Tesla Model 3

### Result:
![query result](https://i.imgur.com/icvnKTt.png)

### Langsmith:
![result on langsmith](https://i.imgur.com/PKsqdXp.png)

## Using the new Tool
Now we can actually use the new `camels_to_tesla_calculator.py`

![new tool's code](https://i.imgur.com/fh6RXoB.png)

### Result:
![new tool usage result](https://i.imgur.com/qHqwiR0.png)
