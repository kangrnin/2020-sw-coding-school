import json
import heapq
import os
from collections import defaultdict
from .path import abs_path
from .prefix_extractor import get_prefix_list

class Indexer:
   def __init__(self, config):
      self.config = config

   def make_prefix(self):
      word_count = defaultdict(int)
      with open(abs_path(self.config['PATH_SOURCE']), 'r', encoding='UTF8') as f:
         for line in f.readlines():
            table = line.maketrans(dict.fromkeys(self.config['PUNCTUATION_CHARS']))
            line = line.translate(table)
            
            for word in line.lower().split():
               word_count[word] += 1
      
      index = defaultdict(list)
      for word, count in sorted(word_count.items()):
         for prefix in get_prefix_list(word, self.config['PREFIX_LENGTH']):
            if len(index[prefix]) < self.config['PQ_SIZE']:
               heapq.heappush(index[prefix], (count, word))
            else:
               heapq.heappushpop(index[prefix], (count, word))
      
      with open(abs_path(self.config['PATH_INDEX']), 'w', encoding='UTF8') as f:
         for prefix in index.keys():
            words = [item[1] for item in heapq.nlargest(self.config['PQ_SIZE'], index[prefix])]
            f.write(prefix+' '+' '.join(words)+'\n')
            # line = prefix + ' '
            # for count, word in heapq.nlargest(self.config['PQ_SIZE'], index[prefix]):
            #    line += word + ' '
            # f.write(line+'\n')

