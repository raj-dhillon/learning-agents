from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from tools.tools import scraper_tool_chunk, read_chunk_file, read_all_chunk_files, search_web_query
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class LearningCrew():
    """Learning crew"""
    agents: List[BaseAgent]
    tasks = List[Task]

    @agent
    def planning_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['planning_agent'],
            verbose=True,
            allow_delegation=True
        )
    
    @agent
    def search_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['search_manager'],
            verbose=True,
            tools=[search_web_query],
            allow_delegation=False
        )
    
    @agent
    def scraping_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['scraping_manager'],
            verbose=True,
            tools=[scraper_tool_chunk],
            allow_delegation=False
        )
            
    @agent
    def researcher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher_agent'],
            verbose=True,
            tools=[read_all_chunk_files],
            allow_delegation=False
        )
    
    @agent
    def summarizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer_agent'],
            verbose=True,
            allow_delegation=False
        )
    
    @task
    def planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['planning_task'],
        )
    
    @task
    def search_manager_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_manager_task'],
        )

    @task
    def scraping_manager_task(self) -> Task:
        return Task(
            config=self.tasks_config['scraping_manager_task'],
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )
    
    @task
    def summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['summary_task'],
            output_file="output/summary.md"
        )
    
    # @crew
    # def crew(self) -> Crew:
    #     return Crew(
    #         agents=self.agents,
    #         tasks=self.tasks,
    #         process= Process.sequential,
    #         verbose=True,
    #     )

    @crew
    def crew(self) -> Crew:
        return Crew(
            # agents=[self.search_manager(), self.scraping_manager(), self.researcher_agent(), self.summarizer_agent()], 
            agents=self.agents,
            # tasks=[self.scraping_manager_task(), self.summary_task()],
            tasks=self.tasks,
            process= Process.sequential,
            verbose=True,
        )