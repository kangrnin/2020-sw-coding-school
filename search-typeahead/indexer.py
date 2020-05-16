import json
import heapq
import os
from collections import defaultdict

import config
from path import abs_path

def make_wordcount():
    word_count = defaultdict(int)

    with open(abs_path(config.path_source_text), 'r', encoding='UTF8') as f:
        for line in f.readlines():
            table = line.maketrans(dict.fromkeys(config.punctuation_chars))
            line = line.translate(table)
            
            for word in line.lower().split():
                word_count[word] += 1

    info = dict()
    with open(abs_path(config.path_info), "r", encoding='UTF8') as f:
        info = json.load(f)
        
    with open(abs_path(config.path_info), "w", encoding='UTF8') as f:
        info["num_unique_words"] = len(word_count.keys())
        info["num_total_words"] = sum(word_count.values())
        f.write(json.dumps(info))

    with open(abs_path(config.path_word_count), "w", encoding='UTF8') as f:
        f.write(json.dumps(word_count, indent=4, sort_keys=True))

def make_prefix():
    with open(abs_path(config.path_word_count), 'r', encoding='UTF8') as f:
        word_count = json.load(f)

    index = defaultdict(list)

    for word, count in word_count.items():
        prefix = ''
        for i in range(0, min(len(word), config.prefix_length)):
            prefix += word[i]
            h = index[prefix] # use list for the prefix as a heap

            if len(h) < config.pq_size:
                heapq.heappush(h, (count, word))
            elif count >= h[0][0]:
                heapq.heappushpop(h, (count, word))
    
    info = dict()
    with open(abs_path(config.path_info), "r", encoding='UTF8') as f:
        info = json.load(f)
        
    with open(abs_path(config.path_info), "w", encoding='UTF8') as f:
        info["num_index"] = len(index.keys())
        index_stat = os.stat(abs_path(config.path_prefix_index))
        info["index_size"] = index_stat.st_size
        f.write(json.dumps(info))
    
    with open(abs_path(config.path_prefix_index), 'w', encoding='UTF8') as f:
        for prefix in index.keys():
            line = prefix + ' '
            for count, word in heapq.nlargest(config.pq_size, index[prefix]):
                line += word + ' '

            f.write(line+'\n')

def index():
    make_wordcount()
    make_prefix()

if __name__ == '__main__':
    index()