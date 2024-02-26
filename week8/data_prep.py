import sys
sys.path.append('../')

from utilities import ChatTemplate
import os

# for honmework 6, please change both values below based on the hw instructions
folder_name = '../signlanguages'
output_file = 'signlanguages_output.jsonl'

template = ChatTemplate.from_file('jsonl.json')
jsonl = ''

for f in os.listdir(folder_name):
    with open(os.path.join(folder_name, f), 'r', encoding="utf-8", errors="ignore") as f:
        text = f.read()

    response = template.completion({'info': text, 'n': '20'})
    jsonl += response.choices[0].message.content.strip() + '\n'

with open(output_file, 'w+') as f:
    f.write(jsonl)