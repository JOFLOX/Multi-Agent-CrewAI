from agents import AIToolsUseAgents
from tasks import AIToolsUseTasks
from file_formated_output import save_markdown
from crewai import Crew, Process
from langchain_community.llms import Ollama


agents = AIToolsUseAgents()
tasks = AIToolsUseTasks()
llm = Ollama(model="openhermes")


# Agents(5)---> supervisor_agent/ searcher_agent/ analyezer_agent/ summarizer_agent/ formatter_agent

maestro = agents.supervisor_agent()
pathfinder = agents.searcher_agent()
sage = agents.analyezer_agent()
mr_white = agents.summarizer_agent()
edna_mode = agents.formatter_agent()


# Tasks(4)---> initial_search_task/ analyze_search_task/ user_guide_summary_task/ linkedin_format_task

initial_search_task = tasks.initial_search_task(pathfinder)
analyze_search_task = tasks.analyze_search_task(sage, [initial_search_task])
user_guide_summary_task = tasks.user_guide_summary_task(mr_white, [analyze_search_task])
linkedin_format_task = tasks.linkedin_format_task(edna_mode, [user_guide_summary_task], save_markdown)


# The Crew

crew = Crew(
    agents=[maestro, pathfinder, sage, mr_white, edna_mode],
    tasks=[initial_search_task, analyze_search_task,user_guide_summary_task, linkedin_format_task ],
    process=Process.hierarchical,
    manager_llm=llm,
    verbose=2
)


# KICKOFF
print("START KICKOFF")
result = crew.kickoff()

print("Crew work results: ")
print(result)
