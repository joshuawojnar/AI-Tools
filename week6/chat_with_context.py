import sys
sys.path.append('../')

from utilities import ChatTemplate

chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are an AI chat program.'},
                  {'role': 'user', 'content': '{{prompt}}'}]})

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    # store the user prompt to memory as history / context
    chat.template['messages'].append({'role': message.role, 'content': message.prompt})
    # call the model with the user prompt
    #   note that the model is already pre-loaded with our chat template
    message = chat.completion({'prompt': prompt}).choices[0].message

    print(f'{message.role}: {message.content}')
    # store the model response to memory as history / context
    chat.template['messages'].append({'role': message.role, 'content': message.content})