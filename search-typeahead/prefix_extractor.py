import re
from jamo import h2j, j2hcj

def get_prefix_list(word, prefix_length):
   prefix_list = list()
   # korean
   if len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', word)) > 0:
      word = word[:prefix_length]
      eumjeol = j2hcj(h2j(word))
      for i in range(0, len(eumjeol)):
         prefix_list.append(eumjeol[:i+1])
   # other language
   else:
      for i in range(0, min(len(word), int(prefix_length))):
         prefix_list.append(word[:i+1])
   
   return prefix_list

if __name__ == '__main__':
   print(get_prefix_list(input(), input()))