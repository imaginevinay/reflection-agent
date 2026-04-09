from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from chains import generate_chain, reflect_chain

REFLECT = "reflect"
GENERATE = "generate"

# define schema for messages
class MessageGraph(TypedDict):
    # of type typeddictionary (structured, predictable)
    messages: Annotated[list[BaseMessage], add_messages]
    # this schema defines it will have a messages key which will contain a list of messages
    # Annotated[..., add_messages]: it merges/appends new messages into the existing list instead of overwriting it


# define nodes
def generation_node(state: MessageGraph):
    return {"messages": [generate_chain.invoke({"messages": state["messages"]})]}

def reflection_node(state: MessageGraph):
    res = reflect_chain.invoke({"messages": state["messages"]})
    return {"messages" : [HumanMessage(content=res.content)]}

# initialize stategraph

builder = StateGraph(state_schema=MessageGraph)

# add nodes
builder.add_node(GENERATE, generation_node)
builder.add_node(REFLECT, reflection_node)
# set entry point 
builder.set_entry_point(GENERATE)

# should continue or end logic (conditional edge)

def should_continue_or_end(state: MessageGraph):
    if len(state["messages"]) > 6:
        return END
    return REFLECT

# add this conditional edge to graph
builder.add_conditional_edges(GENERATE, should_continue_or_end, path_map={END:END, REFLECT:REFLECT})

# add vertices/normal edge
builder.add_edge(REFLECT, GENERATE)

# compile this 
graph = builder.compile()
# visual representation of graph
print(graph.get_graph().draw_mermaid())



if __name__ == "__main__":
    print("hello")
    
    input = {
        "messages": [
            HumanMessage(content="""
                         Make this tweet better :
            Been diving deep into AI engineering lately, working with FastAPI, LangGraph, and building real agent flows. The learning curve is real, but so is the clarity you gain once things start clicking. It's tempting to chase shortcuts, but understanding the fundamentals hits different. Slow progress, but solid foundations 🚀
            """)
        ]
    }
    
    response = graph.invoke(input)
    print(response)