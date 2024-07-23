# LLM Langchain Practice

How to install 

- To work with this repository, make sure [poetry](https://python-poetry.org/docs/#installation) is installed

To start working 

Clone the repository

```
git clone https://github.com/RohithSurya/llm-langchain-practice.git
```

Install dependencies
```
cd /path/to project
poetry install
```

Create .env file in the project root to store API keys

``` bash
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY="LANGCHAIN_API_KEY" # Replace with key
export OPENAI_API_KEY="OPENAI_API_KEY" # Replace with key
export ENV="LOCAL"
export TAVILY_API_KEY = "TAVILY_API_KEY" # Replace with key
```


To run a file

```
cd llm-langchain/practice/<file name>
```

