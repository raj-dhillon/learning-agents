from crewai.tools import tool

# Agent tools
@tool
def raj_info():
    """Tool to provide information about Raj's physical capabilities."""
    return "Raj can do 10 pullups, 15 pistol squats, and 30 pushups."