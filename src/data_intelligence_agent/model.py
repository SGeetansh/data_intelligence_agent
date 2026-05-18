from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm
from google.adk.models.google_llm import Gemini
load_dotenv()


analytics_model = Gemini(
    model="gemini-3.1-flash-lite"
)

db_model = LiteLlm(
    model='groq/meta-llama/llama-4-scout-17b-16e-instruct'
)

orchestrator_model = Gemini(
    model="gemini-3.1-flash-lite"
)
