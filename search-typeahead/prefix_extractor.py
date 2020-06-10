import re
from jamo import h2j, j2hcj

def get_prefix_list(word, prefix_length):
   prefix_list = list()
   word = word[:prefix_length]
   alphabets = j2hcj(h2j(word))
   for i in range(0, len(alphabets)):
      prefix_list.append(alphabets[:i+1])
   return prefix_list

if __name__ == '__main__':
   print(get_prefix_list(input(), input()))