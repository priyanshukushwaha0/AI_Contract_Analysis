from dataclasses import dataclass
import os
from dotenv import load_dotenv
load_dotenv()

@dataclass
class Config:
    provider="gemini"
    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY","")
    limit=50