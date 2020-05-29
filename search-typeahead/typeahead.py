import json
import config
from path import abs_path

f = open(abs_path(config.path_prefix_index), 'r', encoding='UTF8')

index = dict()
for line in f.readlines():
   tokens = line.split()
   # tokens[0] = prefix, tokens[1:] = typeahead
   index[tokens[0]] = tokens[1:]

def get_typeahead(prefix):
   try:
      return json.dumps({'result': 'success', 'typeahead': index[prefix]})
   except:
      return json.dumps({'result': 'failure'})

if __name__ == '__main__':
   print('input prefix. type -1 to exit')
   while prefix := input() != '-1':
      print(index[prefix])
