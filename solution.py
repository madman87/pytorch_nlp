import json

with open("out.json","r") as f:
    for line in f:
        jsn = json.loads(line)
        paragraph = jsn['body']
        words = jsn['words']
        
        # do some magic
