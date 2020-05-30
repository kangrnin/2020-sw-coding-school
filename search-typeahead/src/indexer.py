import json
import heapq
from os.path import abspath

def make_wordcount():
    f = open('text.txt', 'r', encoding='UTF8')

    word_count = dict()

    while True:
        line = f.readline()

        if not line:
            break

        # temporary code. will apply regex later
        punctuation_chars = ['=','_', ';', ':', '!', '?', '.', ',', '—', '*', '[', ']', '{', '}', '(', ')', '#', '$', '%', '`', '&', '"', "'", '”']
        
        for char in punctuation_chars:
            line = line.replace(char, '')
        
        for word in line.lower().split():
            if word in word_count.keys():
                word_count[word] = word_count[word] + 1
            else:
                word_count[word] = 1

    f.close()
    f = open("word-count.txt", "w")
    f.write(json.dumps(word_count, indent=4, sort_keys=True))
    f.close()

def make_prefix():
    f = open('word-count.txt', 'r', encoding='UTF8')

    word_count = json.load(f)
    f.close()

    index = dict()

    # configuration
    prefix_length = 5
    max_num = 8

    for word, count in word_count.items():
        
        for last in range(1, min([len(word)+1, prefix_length+1])):
            prefix = word[:last]

            if prefix not in index.keys():
                index[prefix] = list()

            h = index[prefix]

            # implement fixed size priority queue with min heap 
            if len(h) < max_num:
                heapq.heappush(h, (count, word))
                
            #if word count is larger than smallest value in heap
            elif count >= h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, (count, word))

    f = open('prefix.txt', 'w', encoding='UTF8')

    # delimeters
    delim_header = '#'
    delim_prefix_before ='@'
    delim_prefix_after = '='
    delim_word = ','

    config = dict()
    config['version'] = 1.1
    config['prefix_length'] = prefix_length
    config['max_num'] = max_num
    # write config as json
    f.write(json.dumps(config))

    # end of header
    f.write(delim_header)

    for prefix, heap in index.items():
        batch = delim_prefix_before
        batch += prefix
        batch += delim_prefix_after
        
        count_word = heapq.nlargest(max_num, index[prefix])
        for count, word in count_word[:-1]:
            batch += word + delim_word

        # word of last count_word without delim
        batch += count_word[-1][1]
        f.write(batch)

    f.close()
