import sys
sys.path.append('../')

from utilities import ChatTemplate
import os

# for honmework 6, please change both values below based on the hw instructions
folderName = '../signlanguages'
outputFile = 'signlanguages.jsonl'

template = ChatTemplate.from_file('jsonl.json')
jsonl = ''

for f in os.listdir(folderName):
    with open(os.path.join(folderName, f), 'r') as f:
        text = f.read()

    response = template.completion({'info': text, 'n': '20'})
    jsonl += response.choices[0].message.content.strip() + '\n'

with open(outputFile, 'w+') as f:
    f.write(jsonl)