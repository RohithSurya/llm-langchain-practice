import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.chat_history import (
    InMemoryChatMessageHistory,
)


from langchain_core.runnables import RunnableWithMessageHistory

dotenv.load_dotenv()

store = {}


def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You're a system who greets people in {language}"),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
config = {"configurable": {"session_id": "1"}}

chain = template | model | parser
# resp = chain_with_history.invoke([HumanMessage("My name is surya")], config=config)
# print(resp)

with_chain_history = RunnableWithMessageHistory(
    chain, get_session_history=get_session_history, input_messages_key="messages"
)


resp = with_chain_history.invoke(
    {"messages": [HumanMessage("My name is surya")], "language": "telugu"},
    config=config,
)
print(store)

# print(store)
