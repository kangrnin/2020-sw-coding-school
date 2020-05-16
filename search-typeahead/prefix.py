import json
f = open('../prefix.txt', 'r', encoding='UTF8')

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

def get_suggestion(prefix):
   try:
      return json.dumps({'result': 'success', 'suggestion': index[prefix]})
   except:
      return json.dumps({'result': 'failure'})
