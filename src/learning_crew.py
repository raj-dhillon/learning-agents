from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from tools.scraper import selenium_scraper
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class LearningCrew():
    """Learning crew"""
    agents: List[BaseAgent]
    tasks = List[Task]

    @agent
    def researcher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher_agent'],
            verbose=True,
            tools=[selenium_scraper]
        )
    
    @agent
    def summarizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer_agent'],
            verbose=True,
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )
    
    @task
    def summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['summary_task'],
            output_file="output/summary.md"
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process= Process.sequential,
            verbose=True
        )