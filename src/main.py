import sys
from crew import LearningCrew

# run: python3 src/main.py "what are the different types of swords?"
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 src/main.py \"<question>\"")
        sys.exit(1)

    question = sys.argv[1]

    inputs = {
    "topic": question
}
    results = LearningCrew().crew().kickoff(inputs=inputs)
    print(results)
    exit(0)