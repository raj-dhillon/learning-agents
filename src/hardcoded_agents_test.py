from crewai import Agent, Task, Crew
from tools.tools import raj_info
import dotenv
import os

# Load environment variables from .env file
dotenv.load_dotenv()

# Get the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key is not set in the environment variables.")

# Initialize the CrewAI agents
ans_agent = Agent(
    role="Answerer",
    goal="Provide a concise and accurate answer based on the information gathered.",
    backstory="An expert at synthesizing information and providing clear answers.",
    verbose=True,
    tools=[raj_info],  # Register the raj_info tool
)

# Initialize the CrewAI task
question = "How many squats can raj do?"
ans_task = Task(description=f"Answer the question: {question}", agent=ans_agent, expected_output="a string containing the answer")

# CrewAI Crew setup
crew = Crew(
    agents=[ans_agent],
    tasks=[ans_task],
)

result = crew.kickoff()

print("Result:", result)