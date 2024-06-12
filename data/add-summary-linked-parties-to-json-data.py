
# Python program to read
# json file
# manually replace all \' and \\m
# add links from summaries

# starting count
# len nodes:  345 , len links: 385 385 385
# len nodes:  345 , len links: , len(links):  385 ,len(globalLinks):  385 len(globalLinkStrings):  385
# ending
# len(nodes):  345 , len(all_links): 1506 , len(globalLinks):  1506 , len(globalLinkStrings): 1506

import json
import re
links = None
count = 0
data = {}
# data['comments'] = {}
all_the_links = []
sourceTarget = {}
link_count_dict = {}
total_links = 0
findall = ''
nodes = []


# given a link object, creates a unique string combining source and target nodes.
def make_link_string(link):
    # print(link)
    source = link['source']
    target = link['target']
    nodestring = ""
    if source < target: # str(link['source']) < str(link['target']):
        nodestring = source + ","+  target #  str(link['source']) + str(link['target'])
    else:
        nodestring = target + "," + source  # str(link['target']) + str(link['source'])
    return nodestring

# Opening JSON string file
# f = open('data-input.json')

json_string_file = open("data-input.json")
json_string = json_string_file.read()
print(len(json_string))

js2 = json_string.replace("\\'", " ")
print(len(js2))

# exit()

# returns JSON object as
# a dictionary

data = json.loads(js2)
json_string_file.close()

nodes = data['nodes']
all_links = data['links']
globalLinks = data['globalLinks']
globalLinkStrings = data['globalLinkStrings']
print("len(nodes): ", len(nodes), ", len(all_links):",  len(all_links), ", len(globalLinks): ", len(globalLinks), ", len(globalLinkStrings):", len(globalLinkStrings) )

# Iterating through the json
# list
revised_nodes = []
revised_links = []
for node in data['nodes']:
    nodeStrings = node['nodeStrings']
    node_id = node['id']
    node_links = node['links']
    # print(node['id'])
    filename = node['id'] + ".shtml"
    try:
        f2 = open("narrative_summaries/" + filename)
        summary = f2.read()
        regex = r"(QD[Ii|Ee]\.\d+)"  # new reference number format
        findall = re.findall(regex, summary)
        print(findall)
    except:
        print("no file for " + filename)
    # revised_nodes.append(node)

    print("node_id = ", node_id, ", findall = ", findall)

    for other_node_id in findall:
        if other_node_id != node_id:
            link_obj = {"source": node_id, "target": other_node_id}
            link_string = make_link_string(link_obj)
            # print(link_obj)
            # print(link_string in globalLinkStrings, link_string in nodeStrings)
            if link_string not in globalLinkStrings:
                globalLinkStrings.append(link_string)
                globalLinks.append(link_obj)
                all_links.append(link_obj)

            if link_string not in nodeStrings:
                nodeStrings.append(link_string)
                node_links.append(link_obj)

    node['nodeStrings'] = nodeStrings
    node['links'] = node_links
    node['linkCount'] = len(nodeStrings)
    revised_nodes.append(node)

# print("globalLinkStrings len = ", len(globalLinkStrings))
# print("globalLinkStrings len = ", len(globalLinkStrings))

data['globalLinkStrings'] = globalLinkStrings
data['links'] = globalLinks
data['globalLinks'] = globalLinks

# globalLinkCount = 0
for node in revised_nodes:
    nodeLinkCount = 0
    node_id = node['id']
    for linkString in globalLinkStrings:
        if node_id in linkString:
            nodeLinkCount += 1
    # globalLinkCount += nodeLinkCount

    node['linkCount'] = nodeLinkCount

data['nodes'] = revised_nodes
# print("globalLinkCount = ", globalLinkCount)
print("len(nodes): ", len(data['nodes']), ", len(all_links):",  len(all_links), ", len(globalLinks): ", len(globalLinks), ", len(globalLinkStrings):", len(globalLinkStrings) )

# print(globalLinkStrings)
s = set(globalLinkStrings)
print("len set = ", len(s))

# exit()

data['nodes'] = revised_nodes

# Closing file
# try:
#     f2.close()
# except:
#     print("can't close f2")

# f = open('data.json')

# returns JSON object as
# a dictionary

with open("data-with-links-from-summaries.json", "w") as outfile:
    json.dump(data, outfile)

# json.write load(f)
# f.close()
