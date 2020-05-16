import json
import heapq
from collections import defaultdict

import config
from path import abs_path

def make_wordcount():
    with open(abs_path(config.path_source_text), 'r', encoding='UTF8') as f:
        word_count = defaultdict(int)

        while line := f.readline():
            table = line.maketrans(dict.fromkeys(config.punctuation_chars))
            line = line.translate(table)
            
            for word in line.lower().split():
                word_count[word] += 1
    
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

    with open(abs_path(config.path_prefix_index), 'w', encoding='UTF8') as f:
        for prefix in index.keys():
            line = prefix + ' '
            for count, word in heapq.nlargest(config.pq_size, index[prefix]):
                line += word + ' '
            
            f.write(line+'\n')

if __name__ == '__main__':
    make_wordcount()
    make_prefix()