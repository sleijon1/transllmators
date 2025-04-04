import os
from typing import Annotated

from dotenv import find_dotenv, load_dotenv
from langchain_core.language_models import BaseChatModel
from langchain_openai import AzureChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

load_dotenv(find_dotenv())


class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


def load_llm() -> (BaseChatModel, BaseChatModel):
    api_version = "2024-10-01-preview"

    default_model = os.getenv("AZURE_OPENAI_LLM_DEPLOYMENT_NAME", "gpt-4o")
    default_llm = AzureChatOpenAI(
        azure_deployment=default_model, temperature=0.0, api_version=api_version
    )

    return default_llm


llm = load_llm()


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()


def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)
    return value["messages"][-1].content


if __name__ == "__main__":
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break
            stream_graph_updates(user_input)
        except:
            # fallback if input() is not available
            user_input = "What do you know about LangGraph?"
            print("User: " + user_input)
            stream_graph_updates(user_input)
            break
