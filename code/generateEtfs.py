import json
import collections

theTags=[]
etfFile=""

with open('../etf.json') as json_file:
    data = json.load(json_file)
    for etf in data:
        etfFile = etfFile + "# " + etf['name'] + "\n" + etf['description'] + "\n\n"


f = open("../etf.md", "w")
f.write(etfFile)
f.close()