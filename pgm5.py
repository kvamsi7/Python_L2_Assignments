

import re #importing re module


pattern = re.compile(r'\w*[aeiou][aeiou]\w*',re.I) 


with open('pgm5.txt','r') as text:
  content = text.readlines()


for con in content:
  if pattern.match(con) != None:
    print(con)
