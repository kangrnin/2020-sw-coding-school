def get_prefix_list(word, prefix_length):
   prefix_list = list()
   for i in range(0, min(len(word), int(prefix_length))):
      prefix_list.append(word[:i+1])

   return prefix_list

if __name__ == '__main__':
   print(get_prefix_list(input(), input()))