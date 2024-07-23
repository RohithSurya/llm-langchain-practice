import dotenv
from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
)
from langchain_core.runnables import RunnablePassthrough


from langchain_core.documents import Document
from langchain_chroma import Chroma

dotenv.load_dotenv()

documents = [
    Document("I don't like cats", metadata={"source": "cats-doc"}),
    Document("Apple makes good iphones", metadata={"source": "apple-doc"}),
    Document(
        "Microsoft computer phone corporation is one of the leading technology company",
        metadata={"source": "microsoft-doc"},
    ),
    Document(
        "I like android tablets",
        metadata={"source": "android-doc"},
    ),
    Document("Oranges are good source of Vitamin C", metadata={"source": "fruit-doc"}),
    Document("An apple a day keeps doctor away", metadata={"source": "fruit-doc"}),
]

vector_store = Chroma.from_documents(documents=documents, embedding=OpenAIEmbeddings())
# resp = vector_store.similarity_search("I like iphone")

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Answer the question based on the context: {context}"),
        (
            "human",
            "{question}",
        ),
    ]
)


model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

chain = (
    {"context": retriever, "question": RunnablePassthrough()} | prompt | model | parser
)

resp = chain.invoke("Get content about apple company")
print(resp)
