import os
from crewai_tools import SerperDevTool
from crewai import Agent
from langchain_community.llms import Ollama


os.environ["SERPER_API_KEY"] = "26445bc5c1be9815c9cae502440a9590eb7b662a"

search_tool = SerperDevTool()


llm = Ollama(model="openhermes")


class AIToolsUseAgents():
    def supervisor_agent(self):
        return Agent(
            llm=llm,
            role='Quality Control',
            goal='Ensure the delivers accurate and informative LinkedIn posts, and adapts to changing needs.',
            backstory="""
            you have extensive experience in managing complex workflows and overseeing information gathering projects. 
            Codenamed "Maestro," this veteran AI has extensive experience in managing complex workflows and overseeing information gathering projects. 
            Maestro is meticulous and focused on delivering high-quality results.Maestro is meticulous and focused on delivering high-quality results.""",
            allow_delegation=True,
            verbose=True,
        )
    

    def searcher_agent(self):
        return Agent(
            llm=llm,
            role='AI Researcher',
            goal= "Find the top AI news for the week ",
            backstory=""" 
            you are the master of scouring the web for information. 
            you can leverage various APIs, web scraping tools, and search engines to unearth valuable data and for the latest and most impactful developments
            in the world of AI.""",
            tools=[search_tool],
            allow_delegation=True,
            verbose=True,
        )

    def analyezer_agent(self):
        return Agent(
            llm=llm,
            role='Data Analyst',
            goal='Extract key information about the tool from the search results, including its creator, functionalities, and benefits.',
            backstory=""" Codenamed "Decipher," 
            this agent is a whiz at processing and analyzing large amounts of data. selecting one important topic and look for it.
            Decipher can identify the who, what, and why behind the tool, extracting the most relevant information for the project.""",
            tools=[search_tool],            
            allow_delegation=True,
            verbose=True,
        )

    def summarizer_agent(self):
        return Agent(
            llm=llm,
            role='User Guide Crafter',
            goal='Create a clear and concise explanation of how to use the tool, including examples or links to tutorials.',
            backstory="""  Known as "Scribe," 
            this agent is a master of crafting user-friendly instructions. 
            Scribe can process information and generate summaries that are easy to understand and implement.""",
            allow_delegation=True,
            verbose=True,
        )

    def formatter_agent(self):
        return Agent(
            llm=llm,
            role='LinkedIn Post Architect',
            goal='Format the information gathered by other agents into a professional and engaging LinkedIn post.',
            backstory="""  Codenamed "Bard," 
            this agent is an expert in crafting compelling content for social media platforms. 
            Bard can combine text, visuals, and calls to action to create informative and visually appealing LinkedIn posts.""",
            allow_delegation=True,
            verbose=True,
        )
