import sys
sys.path.append('../')

from utilities import Template

response = Template.from_file('lawyer.json').completion(
    {'action': 'draft',
     'document': 'a nondisclosure agreement (NDA) between two parties'})

print(response.choices[0].text)