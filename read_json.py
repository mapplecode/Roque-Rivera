import json

# Opening JSON file
f = open('samples.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data:
    print(i['File Name'], ' ',i['Pdf Type'])


# Closing file
f.close()