import heapq
import os
from collections import defaultdict
import json
from .path import abs_path
from .prefix_extractor import get_prefix_list

class Typeahead:
   config = dict()
   def __init__(self, config):
      self.config = config
      f = open(abs_path(config['PATH_PREFIX_INDEX']), 'r', encoding='UTF8')

      self.index = defaultdict(list)
      for line in f.readlines():
         tokens = line.split()
         # tokens[0] = prefix, tokens[1:] = typeahead
         self.index[tokens[0]] = tokens[1:]

   def get_typeahead(self, prefix):
      if prefix in self.index:
         return {'result': 'success', 'typeahead': self.index[prefix][:5]}
      else:
         return {'result': 'failure'}
   
   def apply_changes(self):
      index_new = self.index
      with open(abs_path(self.config['PATH_PREFIX_UPDATE']), 'r', encoding='UTF8') as f:
         for word in set(f.read().splitlines()):
            for prefix in get_prefix_list(word, self.config['PREFIX_LENGTH']):
               index_new[prefix].insert(0, word)
      
      with open(abs_path(self.config['PATH_PREFIX_DELETE']), 'r', encoding='UTF8') as f:
         for word in set(f.read().splitlines()):
            for prefix in get_prefix_list(word, self.config['PREFIX_LENGTH']):
               if prefix in index_new and word in index_new[prefix]:
                  index_new[prefix].remove(word)

      # delete file contents
      open(abs_path(self.config['PATH_PREFIX_UPDATE']), 'w').close()
      open(abs_path(self.config['PATH_PREFIX_DELETE']), 'w').close()

      self.index = index_new

if __name__ == '__main__':
    index()