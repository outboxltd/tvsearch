import json
from pprint import pprint

# open the file
with open('./data/143.json') as the_file:
    data = json.load(the_file)

episodes = data['_embedded']['episodes']

# print(data)

# for i in data:
#     pprint(i['url']);

# for i in data['_embedded']['episodes']:
#    print(i)

# get images
# for i in data['_embedded']['episodes']:
#    print(i['image']['medium'])

# get images
# for i in data['_embedded']['episodes']:
#    print(i['image']['medium'])

# get images
# for i in data['_embedded']['episodes']:
#    print(i['name'])


for i in episodes:
   print(i['name'])