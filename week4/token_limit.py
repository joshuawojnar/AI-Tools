import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = 'What is American Sign Language?'

response = openai.chat.completions.create(
    model='gpt-3.5-turbo',
    max_tokens=20,  # a very small value
    messages=[{'role': 'user', 'content': prompt}])

print(response.choices[0].message.content)