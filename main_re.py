import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
)

dotenv.load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()
template = ChatPromptTemplate.from_messages(
    [
        ("system", "Translate the following to the {language} language"),
        ("human", "{text}"),
    ]
)

chain = template | model | parser

print(chain.invoke({"language": "telugu", "text": "How are you"}))
