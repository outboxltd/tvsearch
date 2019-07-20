import json
from pprint import pprint

# open the file
with open('./data/143.json') as the_file:
    data = json.load(the_file)

# print(data)

# for i in data:
#     pprint(i['url']);

for i in data['_embedded']['episodes']:
   print(i['url'])