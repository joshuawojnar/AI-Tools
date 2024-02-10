import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = 'Write a short story about a deaf scientist who saved the world using sign language.'

response = openai.chat.completions.create(
    model='gpt-3.5-turbo',
    temperature=0.1,
    max_tokens=100,
    messages=[{'role': 'user', 'content': prompt}])

print(response.choices[0].message.content)