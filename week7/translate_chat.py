import sys
sys.path.append('../')

from utilities import ChatTemplate

response = ChatTemplate.from_file(
    'translate.json').completion({'text': "Live long and prosper!"})

print(response.choices[0].message.content)