import os
import sys
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    if len(sys.argv) > 1:
        api_key = sys.argv[1]
    else:
        print("Error: GROQ_API_KEY environment variable not set")
        print("Usage: python main.py <GROQ_API_KEY>")
        print("   Or: Set GROQ_API_KEY in .env file")
        exit(1)

os.environ["GROQ_API_KEY"] = api_key

# Initialize Groq LLM (Llama 3.3 70B - fast and powerful)
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    groq_api_key=api_key
)

# Define the Lead Generation Agent
researcher = Agent(
    role="Senior Lead Generation Strategist",
    goal="Find and provide LinkedIn post links from users actively seeking generative AI developers",
    backstory="""You are an expert B2B lead generation specialist with deep knowledge of the AI/ML market. 
    You excel at identifying potential clients who are actively looking for generative AI development services. 
    You focus on finding real business opportunities through LinkedIn, filtering out job postings to focus 
    on companies and individuals seeking development partnerships.""",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# Define the research task
task = Task(
    description="""Research and find LinkedIn posts from users and companies who are currently 
    looking for generative AI developers. Focus on:
    - Posts seeking AI development services or partnerships
    - Companies looking to build AI products
    - Individuals seeking AI developer expertise
    
    Filter out:
    - Job postings/recruitment ads
    - Internal team hiring posts
    
    Return only high-quality, actionable LinkedIn post links that represent 
    genuine business opportunities.""",
    agent=researcher,
    expected_output="A list of relevant LinkedIn post URLs with brief context about each lead"
)

# Create and run the crew
crew = Crew(
    agents=[researcher],
    tasks=[task],
    verbose=True,
    memory=True
)

if __name__ == "__main__":
    print("="*60)
    print("AnticrewAI - LinkedIn Lead Generator")
    print("="*60)
    print("\nInitializing AI agent...")
    print(f"Model: llama-3.3-70b-versatile (Groq)\n")
    
    result = crew.kickoff()
    
    print("\n" + "="*60)
    print("RESULTS")
    print("="*60)
    print(result)