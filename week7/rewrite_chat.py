import sys
sys.path.append('../')

from utilities import ChatTemplate

sample = '''
Deep in the shady sadness of a vale
Far sunken from the healthy breath of morn,
Far from the fiery noon, and eve's one star,
Sat gray-hair'd Saturn, quiet as a stone,
Still as the silence round about his lair;
Forest on forest hung about his head
Like cloud on cloud. No stir of air was there,
Not so much life as on a summer's day
Robs not one light seed from the feather'd grass,
But where the dead leaf fell, there did it rest.
A stream went voiceless by, still deadened more
By reason of his fallen divinity
Spreading a shade: the Naiad 'mid her reeds
Press'd her cold finger closer to her lips.'''

text = "Gallaudet University, federally chartered in 1864, is a bilingual, diverse, multicultural institution of higher education that ensures the intellectual and professional advancement of deaf and hard of hearing individuals through American Sign Language (ASL) and English."

response = ChatTemplate.from_file('rewrite.json').completion({'sample': sample, 'text': text})

print(response.choices[0].message.content)