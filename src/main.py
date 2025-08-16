import sys
import os
from learning_crew import LearningCrew
from src.scraping_crew import ScrapingCrew

# run: python3 src/main.py "what are the different types of swords?"
def run_scraping_crew(question):
    inputs = {
        "topic": question,
        "website_url": "https://terraria.wiki.gg/wiki/Weapons"
    }
    results = ScrapingCrew().crew().kickoff(inputs=inputs)
    print(results)

def run_learner_crew(question):
    os.makedirs("output", exist_ok=True)
    inputs = {
        "topic": question,
        "website_url": "https://themagicians.fandom.com/wiki/Quentin_Coldwater"
    }
    results = LearningCrew().crew().kickoff(inputs=inputs)

    # Print results
    print("\n\n=== FINAL REPORT ===\n\n")
    print(results)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 src/main.py <crew> \"<question>\"")
        sys.exit(1)

    crew_name = sys.argv[1]
    question = sys.argv[2]

    if crew_name == "scraper":
        run_scraping_crew(question)
    elif crew_name == "learner":
        run_learner_crew(question)
    else:
        print("Invalid crew selection, choose: *scraper* or *learner*.")
        sys.exit(1)
