from os import environ as env
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = env['OPENAI_API_KEY']
res = openai.Embedding.create(
  model="text-embedding-ada-002",
  input="The food was delicious and the waiter..."
)
print(res)
