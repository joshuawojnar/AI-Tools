import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

# for homework 6, please change this to your own model
modelName = 'ft:davinci-002:personal::8vTNUS40'

template = '''You are a Q&A bot. You provide short answers to questions.
For example:
Question: What does ASL stand for? American Sign Language.
Provide the answer to the following question:
Question: '''

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    response = openai.completions.create(
        model= modelName,
        temperature=0,
        stop=['\n'],
        prompt=template + prompt)
    print(response.choices[0].text)
