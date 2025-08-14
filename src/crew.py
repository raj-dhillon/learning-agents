from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import SeleniumScrapingTool
from tools.scraper import selenium_scraper
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from tools.tools import raj_info

@CrewBase
class LearningCrew():
    """Learning crew"""
    agents: List[BaseAgent]
    tasks = List[Task]

    # @agent
    # def answerer(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['answerer'],
    #         verbose=True,
    #         tools=[raj_info]
    #     )
    
    # @task
    # def answerer_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['answerer_task']
    #     )
    @agent
    def wiki_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['wiki_scraper'],
            verbose=True,
            tools=[selenium_scraper]
        )
    
    @task
    def wiki_scraper_task(self) -> Task:
        return Task(
            config=self.tasks_config['wiki_scraper_task']
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=False
        )