import os
from getpass import getpass
from dotenv import load_dotenv

from crewai import Agent,Task,Crew,Process
from crewai_tools import SerperDevTool
from langchain_groq import ChatGroq

import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)
# warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore")


dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path)

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="gemma2-9b-it",groq_api_key=GROQ_API_KEY)
print(llm.invoke("hi"))
