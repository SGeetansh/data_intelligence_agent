from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

model = LiteLlm(
    model='groq/meta-llama/llama-4-scout-17b-16e-instruct'
)