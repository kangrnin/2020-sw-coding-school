if __name__ == "__main__":
    
    f = open('prefix.txt', 'r', encoding='UTF8')

    index = dict()

    # will later include delimeters to header
    # and use them instead of hard coding
    tokens = f.read().split('#')[1].split('@')

    for token in tokens:
        prefix_words = token.split('=')
        prefix = prefix_words[0]

        words = []
        if len(prefix_words) == 2:
            words = token.split('=')[1].split(',')
            
        index[prefix] = words

    print('type any prefix. type -1 to exit')

    while True:
        prefix = input()

        if prefix == '-1':
            exit()
        if prefix == '':
            continue

        try:
            print(index[prefix])
        except:
            print('word for the prefix doesn''t exist')
