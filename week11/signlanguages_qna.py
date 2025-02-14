import sys
sys.path.append('../')

from utilities import ChatTemplate, get_embedding, cosine_distance
import json

embeddings = json.load(open('embeddings.json', 'r'))

def nearest_embedding(embedding):
    nearest, nearest_distance = None, 1

    for path, embedding2 in embeddings.items():
        distance = cosine_distance(embedding, embedding2)
        if distance < nearest_distance:
            nearest, nearest_distance = path, distance

    return nearest

chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are a Q&A AI.'},
                  {'role': 'system', 'content': 'Here are some facts that can help you answer the following question: {{data}}'},
                  {'role': 'user', 'content': '{{prompt}}'}]})

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    context = nearest_embedding(get_embedding(prompt))
    data = open(context, 'r').read()

    message = chat.completion(
        {'data': data, 'prompt': prompt}).choices[0].message

    print(f'{message.role}: {message.content}')