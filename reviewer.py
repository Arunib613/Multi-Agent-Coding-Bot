from llm import llm
from state import AgentState

PROMPT = "Reviw the following HTML code for any errors or improvements:\n\n{}"

def reviewer(state: AgentState):
    result = llm.invoke(PROMPT.format(state["code"]))
    print("Code Generated Successfully")
    return {"review": result.content}