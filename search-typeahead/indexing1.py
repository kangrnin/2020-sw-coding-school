import json

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

f = open("word-count.txt", "w")
f.write(json.dumps(word_count, indent=4, sort_keys=True))
