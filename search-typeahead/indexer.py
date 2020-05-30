import json
import heapq
import os
from collections import defaultdict
from .path import abs_path
from .prefix_extractor import get_prefix_list

class Indexer:
   def __init__(self, config):
      self.config = config

   def make_wordcount(self):
      word_count = defaultdict(int)
      with open(abs_path(self.config['PATH_SOURCE_TEXT']), 'r', encoding='UTF8') as f:
         for line in f.readlines():
            table = line.maketrans(dict.fromkeys(self.config['PUNCTUATION_CHARS']))
            line = line.translate(table)
            
            for word in line.lower().split():
               word_count[word] += 1
      
      word_count = sorted(word_count.items())
      with open(abs_path(self.config['PATH_WORD_COUNT']), 'w', encoding='UTF8') as f:
         for word, count in word_count:
            f.write(word+' '+str(count)+'\n')

   def make_prefix(self, index=None):
      # if index not given, make from wordcount
      if not index:
         word_count = dict()
         with open(abs_path(self.config['PATH_WORD_COUNT']), 'r', encoding='UTF8') as f:
            for line in f.readlines():
               tokens = line.split()
               word_count[tokens[0]] = int(tokens[1])

         index = defaultdict(list)
         for word, count in word_count.items():
            for prefix in get_prefix_list(word, self.config['PREFIX_LENGTH']):
               h = index[prefix] # use list for the prefix as a heap

               if len(h) < self.config['PQ_SIZE']:
                  heapq.heappush(h, (count, word))
               elif count >= h[0][0]:
                  heapq.heappushpop(h, (count, word))
         
         with open(abs_path(self.config['PATH_PREFIX_INDEX']), 'w', encoding='UTF8') as f:
            for prefix in index.keys():
               line = prefix + ' '
               for count, word in heapq.nlargest(self.config['PQ_SIZE'], index[prefix]):
                  line += word + ' '
               f.write(line+'\n')
      
      #if index instance is given, write directly to file
      else:
         with open(abs_path(self.config['PATH_PREFIX_INDEX']), 'w', encoding='UTF8') as f:
            for prefix in index.keys():
               line = prefix + ' '
               for word in index[prefix]:
                  line += word + ' '
               f.write(line+'\n')
         

   def update_index(self, prefix):
      with open(abs_path(self.config['PATH_PREFIX_UPDATE']), 'a', encoding='UTF8') as f:
         f.write(prefix+'\n')

   def delete_index(self, prefix):
      with open(abs_path(self.config['PATH_PREFIX_DELETE']), 'a', encoding='UTF8') as f:
         f.write(prefix+'\n')
