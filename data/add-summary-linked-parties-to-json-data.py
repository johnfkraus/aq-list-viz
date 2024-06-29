
# Python program to read a json file
# 1. manually replace all \' and \\m
# 2. add links from summaries

# starting count
# len nodes:  345 , len links: 385 385 385
# len nodes:  345 , len links: , len(links):  385 ,len(globalLinks):  385 len(globalLinkStrings):  385
# ending
# len(nodes):  345 , len(all_links): 1506 , len(globalLinks):  1506 , len(globalLinkStrings): 1506

# june 20, len(nodes):  345 , len(all_links): 1315 , len(globalLinks):  1315 , len(globalLinkStrings): 1315

# june 29  len(nodes):  345 , len(all_links): 1311 , len(globalLinks):  1311 , len(globalLinkStrings): 1311


import json
import re
import csv

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
        nodestring = source + "," + target #  str(link['source']) + str(link['target'])
    else:
        nodestring = target + "," + source  # str(link['target']) + str(link['source'])
    return nodestring


json_string_file = open("data-input.json")
json_string = json_string_file.read()
print(len(json_string))

js2 = json_string.replace("\\'", " ")
print(len(js2))

# exit()
# returns JSON object as a dictionary

data = json.loads(js2)
json_string_file.close()

nodes = data['nodes']
all_links = data['links']
globalLinks = data['globalLinks']
globalLinkStrings = data['globalLinkStrings']
print('START:')
print("len(globalLinkStrings) = ", len(globalLinkStrings))
print("len(nodes): ", len(nodes), ", len(all_links):",  len(all_links), ", len(globalLinks): ", len(globalLinks), ", len(globalLinkStrings):", len(globalLinkStrings) )

# Iterating through the data.json
# list, read each summary file and parse them for links
revised_nodes = []
revised_links = []
no_summary_file_found_for = []
for node in data['nodes']:
    nodeStrings = node['nodeStrings']  # unique link ID, should be called linkStrings, though.
    node_id = node['id']
    node_links = node['links']
    # print(node['id'])
    filename = node['id'] + ".shtml"
    print("start, len nodeStrings = ", len(nodeStrings))

    try:
        narr_summary_file = open("narrative_summaries/" + filename)
        summary = narr_summary_file.read()
        regex = r"(QD[Ii|Ee]\.\d+)"  # new reference number format
        findall = re.findall(regex, summary)
        # print("node_id = ", node_id, ", findall: ", findall)
    except:
        no_summary_file_found_for.append([node_id, node['name'], 'link', 'date'])
        print("no summary file found for ", filename)

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


    node['nodeStrings'] = nodeStrings  # linkStrings
    node['links'] = node_links
    node['linkCount'] = len(nodeStrings)
    revised_nodes.append(node)
    print("finish, len nodeStrings = ", len(nodeStrings))

# print("globalLinkStrings len = ", len(globalLinkStrings))
# print("globalLinkStrings len = ", len(globalLinkStrings))

data['globalLinkStrings'] = globalLinkStrings
data['links'] = globalLinks
data['globalLinks'] = globalLinks

globalNodeLinkCount = 0
for node in revised_nodes:
    nodeLinkCount = 0
    node_id = node['id']
    for linkString in globalLinkStrings:
        if node_id in linkString:
            nodeLinkCount += 1
    # globalLinkCount += nodeLinkCount

    node['linkCount'] = nodeLinkCount
    globalNodeLinkCount += nodeLinkCount

data['nodes'] = revised_nodes
# print("globalLinkCount = ", globalLinkCount)


# print(globalLinkStrings)
s = set(globalLinkStrings)
print("len set = ", len(s))


# returns JSON object as a dictionary

with open("data-with-links-from-summaries.json", "w") as outfile:
    json.dump(data, outfile)

# json.write load(f)
# f.close()
print("len(nodes): ", len(data['nodes']), ", len(all_links):",  len(all_links), ", len(globalLinks): ", len(globalLinks), ", len(globalLinkStrings):", len(globalLinkStrings) )
print("len(globalLinkStrings) = ", len(globalLinkStrings))
print("globalNodeLinkCount = ", globalNodeLinkCount, ", (double counts links, potentially)")
print("len( no_summary_file_found_for = ", len(no_summary_file_found_for))
print("no_summary_file_found_for = ", no_summary_file_found_for)

with open('no_summary_file_found_for.csv', 'w', newline='') as csvfile:
    for csv_row in no_summary_file_found_for:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(csv_row)

print("DONE")