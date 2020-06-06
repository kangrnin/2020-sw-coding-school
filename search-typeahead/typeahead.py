import heapq
import os
from collections import defaultdict
import json
from jamo import h2j, j2hcj
from .path import abs_path, version_path, get_current_version
from .prefix_extractor import get_prefix_list

class Typeahead:
   config = dict()
   def __init__(self, config):
      self.config = config
      self.version = get_current_version()

      with open(version_path(self.config['PATH_INDEX'], self.version), 'r', encoding='UTF8') as f:
         self.index = defaultdict(list)
         for line in f.readlines():
            tokens = line.split()
            # tokens[0] = prefix, tokens[1:] = typeahead
            self.index[tokens[0]] = tokens[1:]

   def get_typeahead(self, prefix):
      prefix = j2hcj(h2j(prefix))
      if prefix in self.index:
         return {'result': 'success', 'typeahead': self.index[prefix][:5]}
      else:
         return {'result': 'failure'}
   
   def update_index(self, word):
      with open(version_path(self.config['PATH_UPDATE'], self.version), 'a', encoding='UTF8') as f:
         f.write(word + '\n')
   
   def delete_index(self, word):
      with open(version_path(self.config['PATH_DELETE'], self.version), 'a', encoding='UTF8') as f:
         f.write(word + '\n')

   def apply_changes(self):
      index_new = self.index
      with open(version_path(self.config['PATH_UPDATE'], self.version), 'r', encoding='UTF8') as f:
         for word in set(f.read().splitlines()):
            for prefix in get_prefix_list(word, self.config['PREFIX_LENGTH']):
               index_new[prefix].insert(0, word)
      
      with open(version_path(self.config['PATH_DELETE'], self.version), 'r', encoding='UTF8') as f:
         for word in set(f.read().splitlines()):
            for prefix in get_prefix_list(word, self.config['PREFIX_LENGTH']):
               if prefix in index_new and word in index_new[prefix]:
                  index_new[prefix].remove(word)

      self.index = index_new
      self.version += 1
      index_path = version_path(self.config['PATH_INDEX'], self.version)
      if not os.path.exists(index_path):
         os.makedirs(os.path.dirname(index_path))
      with open(version_path(self.config['PATH_INDEX'], self.version), 'w', encoding='UTF8') as f:
         for prefix in index_new.keys():
            f.write(prefix + ' ' + ' '.join(index_new[prefix])+'\n')

if __name__ == '__main__':
    index()