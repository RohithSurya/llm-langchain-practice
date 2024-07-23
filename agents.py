import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

dotenv.load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()
search = TavilySearchResults(max_results=2, search_depth="advanced")
search_results = search.invoke("what is the weather in SF")
print(search_results)

tools = [search]
model_with_tools = model.bind_tools(tools=tools)

resp = model_with_tools.invoke("Hi")
print(resp)

resp = model_with_tools.invoke([HumanMessage(content="Hi")])

agent_executor = create_react_agent(model, tools=tools)
resp = agent_executor.invoke(
    {"messages": [HumanMessage("How's the weather in Los Angeles now?")]}
)
print(resp)

response = agent_executor.invoke(
    {"messages": [HumanMessage(content="whats the weather in sf?")]}
)

response = agent_executor.invoke(
    {"messages": [HumanMessage(content="Get latest us election news")]}
)

print(response["messages"])
