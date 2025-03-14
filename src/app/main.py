# ruff: noqa: D100
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig
from dotenv import load_dotenv

load_dotenv()

vertexai.init()

model_config = GenerationConfig(temperature=1, top_p=0.95, max_output_tokens=8192)

with open("src/app/prompt_templates/french_lawyer.txt") as f:
    system_instruction = f.readlines()

model = GenerativeModel(
    "gemini-2.0-flash-lite-001",
    generation_config=model_config,
    system_instruction=system_instruction,
)

def french_lawyer(question: str) -> str:
    """Given a questions, passes it to the LLM and returns the textual answer."""
    answer = model.generate_content(question)
    return answer.text

if __name__ == "__main__":
    print(french_lawyer("Ai-je le droit de boire de l'alcool ?"))