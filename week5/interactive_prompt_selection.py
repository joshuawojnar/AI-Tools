from utilities import ChatTemplate
import json

selection = ChatTemplate.from_file('selection_chat.json')

while True:
    ask = input('ask: ')
    if ask == 'exit':
        break
    
    response = selection.completion({'ask': ask})
    print(response.choices[0].message.content)
    
    content = json.loads(response.choices[0].message.content)

    response = ChatTemplate.from_file(content['as'] + '_chat.json').completion({
        'action': content['action'],
        'document': content['document']})
    print(response.choices[0].message.content)