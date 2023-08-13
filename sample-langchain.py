from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import key

key.setenv()

llm = OpenAI(temperature=0)

tools = load_tools(["serpapi"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

print(agent.run("2023年4月現在の首相の名前は何でしょうか？\n回答は英語から日本語に翻訳してください。"))