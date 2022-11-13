import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

conversation = ""

i = 1

while (i != 0):
  question = input("Human: ")
  conversation += "\nHumano: " + question + "\nAI:"
  response = openai.Completion.create(
    engine="davinci",
    prompt=conversation,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["\n", " Human:", " AI:"]
  )

  answer = response.choices[0].text.strip()
  conversation += answer
  print("AI: " + answer + "\n")