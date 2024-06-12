
# Python program to read
# json file
# manually replace all \' and \\m
import json

# Opening JSON string file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)
f.close()

# Iterating through the json
# list
new_nodes = []
for node in data['nodes']:
    print(node['id'])
    filename = node['id'] + ".shtml"
    try:
        f2 = open("downloaded_request_summaries/" + filename)
        node['summary'] = f2.read()
    except:
        print("no file for " + filename)
    new_nodes.append(node)

data['nodes'] = new_nodes

# Closing file
try:
    f2.close()
except:
    print("can't close f2")

# f = open('data.json')

# returns JSON object as
# a dictionary

with open("data-with-summaries-2.json", "w") as outfile:
    json.dump(data, outfile)

# json.write load(f)
f.close()
