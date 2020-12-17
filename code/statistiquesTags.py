import json
import collections

print("OK")
theTags=[]

with open('/data/sources.json') as json_file:
    data = json.load(json_file)
    for p in data:
        theTags = theTags + p['tags']

print(collections.Counter(theTags))