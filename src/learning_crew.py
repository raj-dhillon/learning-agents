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
    def search_manager_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_manager_task'],
        )

    @task
    def scraping_manager_task(self) -> Task:
        # def orchestrate_research(inputs):
        #     topic = inputs['topic']
        #     website_url = inputs['website_url']
        #     chunk_metadata = scraper_tool_chunk.run(website_url)

        #     research_output = []

        #     for chunk_file in chunk_metadata['chunk_files']:
        #         mini_crew = Crew(
        #             agents=[self.researcher_agent()],
        #             tasks=[self.research_task()],
        #             process=Process.sequential,
        #             verbose=False,
        #         )
        #         result = mini_crew.kickoff(inputs = {'topic': topic, 'filename': chunk_file})
        #         research_output.append(result)

        #     return research_output

        return Task(
            config=self.tasks_config['scraping_manager_task'],
            # callback=orchestrate_research
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
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process= Process.sequential,
            verbose=True,
        )

    # @crew
    # def crew(self) -> Crew:
    #     return Crew(
    #         agents=[self.scraping_manager(), self.summarizer_agent()],
    #         tasks=[self.scraping_manager_task(), self.summary_task()],
    #         process= Process.sequential,
    #         verbose=True,
    #     )