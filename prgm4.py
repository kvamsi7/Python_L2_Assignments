''' Translating each of the following English statements into a regular expression '''

import re

pattern1 = re.compile(r'\d+\w+\d') #digit at the beginning of the string and a digit at the end of the string
pattern2 = re.compile(r'(\s|\w)') #A string that contains only whitespace characters or word characters
pattern3 = re.compile(r'(\S)') #A string containing no whitespace characters


matches1 = pattern1.finditer(' Hi this is vam and my numbers are 9adfa9 9014558531')
matches2 = pattern2.finditer('Hi this is @vam')
matches3 = pattern3.finditer('Hi this is vam')


for match in matches1: # iteration every match that found 
    print(match)
    
for match in matches2:
    print(match)

for match in matches3:
    print(match)