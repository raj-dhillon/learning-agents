from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from tools.tools import raj_info

@CrewBase
class LearningCrew():
    """Learning crew"""
    agents: List[BaseAgent]
    tasks = List[Task]

    @agent
    def answerer(self) -> Agent:
        return Agent(
            config=self.agents_config['answerer'],
            verbose=True,
            tools=[raj_info]
        )
    
    @task
    def answerer_task(self) -> Task:
        return Task(
            config=self.tasks_config['answerer_task']
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True
        )