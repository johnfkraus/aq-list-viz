# Databricks notebook source
# MAGIC %md
# MAGIC /Volumes/main/default/example-data/AQList.xml
# MAGIC
# MAGIC /Volumes/main/default/example-data/7v9bhen-al-qaida.xml
# MAGIC
# MAGIC /Volumes/main/default/example-data/links.csv
# MAGIC

# COMMAND ----------

import json
class Link:
    def __init__(self, ref1, ref2):
        if ref1 != ref2:
            if ref1 < ref2:
                self.__link_tuple = (ref1, ref2)
            else:
                self.__link_tuple = (ref2, ref1)
        else:
            raise SyntaxError("error ref1 equals ref2")

    def __eq__(self, other):
        if not isinstance(other, Link):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return (self.__link_tuple[0] == other.__link_tuple[0] ) and (self.__link_tuple[1] == other.__link_tuple[1])

    def __str__(self) -> str:
        # stringreplist = []
        # for item in self.linkset:
        #    stringreplist.append(item)
        # return ",".join (stringreplist)
        return str(self.__link_tuple)


    def __hash__(self):
        return hash(self.__link_tuple)

    def get_link_object(self):
        link_object = {}
        link_object['source'] = self.__link_tuple[0]
        link_object['target'] = self.__link_tuple[1]
        return link_object

    def get_json(self):
        return json.dumps(self.get_link_object())
      

def test_link():
    set_of_links = set()
    l1 = Link("abc", "def")
    print('l1 = ', l1)
    l2 = Link("def", "abc")
    print('l2 = ', l2)
    print(l1==l2)
    print(set_of_links.add(l1))
    print(set_of_links.add(l2))
    print('len(set_of_links) = ' , len(set_of_links))
    #     myset = set((l1, l2))
    #     print('myset = ', myset)
    l3 = Link("def", "ckz")
    print('l3 = ', l3)
    print(l2==l3)
    set_of_links.add(l3)
    print('len(set_of_links) = ' , len(set_of_links))
    #l4 = Link("def", "def")  # should fail
    l5 = Link("qqq", "uuu")
    set_of_links.add(l5)
    print('len(set_of_links) = ' , len(set_of_links))
    print(set_of_links)
    print([str(l) for l in set_of_links])
    print(l1.get_link_object())
    print(l1.get_json())
    
test_link()

# COMMAND ----------

# read xml file
# spark.read.format("json").load("/Volumes/my_catalog/my_schema/my_volume/data.json").show()
volpath = "/Volumes/main/default/example-data/7v9bhen-al-qaida.xml"
indiv_sdf = spark.read.option("rowTag", "INDIVIDUAL").format("xml").load(volpath) # .show()
ent_sdf = spark.read.option("rowTag", "ENTITY").format("xml").load(volpath) # .show()

# COMMAND ----------

import csv
csv_filepath = "/Volumes/main/default/example-data/links.csv"

link_sdf = spark.read.csv(csv_filepath, header=True)
link_sdf.createOrReplaceTempView("links_table")
reference_number = 'QDi.001'
query = "SELECT link from links_table WHERE ref_num='{}'".format(reference_number)
summary_link = spark.sql(query)

print(summary_link.first()[0])


# COMMAND ----------

indiv_coll = indiv_sdf.collect()
print(type(indiv_coll))
print(len(indiv_coll))
# print(indiv_coll)
ent_coll= ent_sdf.collect()
print(len(ent_coll))

# COMMAND ----------

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
# sourceTarget['QDi.9999'] = ['TEST FAKE DATA'] # for testing only; to be deleted
for collection in [indiv_coll, ent_coll]:
    for row in collection:  # indiv_coll:
        reference_number = ''
        rowAsDict = row.asDict()
        # print(row.asDict())
        has_nat2 = False
        node = {}
        if row['DATAID']:
            node['DATAID'] = str(row['DATAID'])
        else:
            print("No DATAID!")
        node['linkCount'] = 0

        count += 1

        full_name = ''
        if 'SECOND_NAME' in rowAsDict.keys():
            for name in [row['FIRST_NAME'], row['SECOND_NAME'],row['THIRD_NAME'], row['FOURTH_NAME']]:
                if name:
                    full_name = full_name + " " + name
            full_name = full_name.strip()
        else:
            full_name = row['FIRST_NAME']

        reference_number = row['REFERENCE_NUMBER'].rstrip('.')
        node['REFERENCE_NUMBER'] = reference_number.strip()
        node['id'] = reference_number        

        # print("reference_number:", reference_number)
        query = "SELECT link from links_table WHERE ref_num='{}'".format(reference_number)
        link_result = spark.sql(query)
        if link_result.isEmpty():
            node['summary_link'] = "None"
        else:
            summary_link = spark.sql(query).first()[0]
            # print("summary_link: ", summary_link)
            node['summary_link'] = summary_link
 

        # print(summary_link.first()[0])
        # summary_link = spark.sql("SELECT link FROM links WHERE ref_num = reference_number")

        full_name = full_name.replace('\n', ' ')
        full_name = re.sub(' +', ' ', full_name)

        node['name'] = full_name

        name_original_script = row['NAME_ORIGINAL_SCRIPT']
        if name_original_script:
            name_original_script.replace('\n', ' ')
            name_original_script = re.sub(' +', ' ', name_original_script)
            node['NAME_ORIGINAL_SCRIPT'] = name_original_script #  row['NAME_ORIGINAL_SCRIPT']
        else:
            node['NAME_ORIGINAL_SCRIPT'] = ''

        if reference_number.startswith("QDi"):
            node['indiv0OrEnt1'] = 0 
        elif reference_number.startswith("QDe"):
            node['indiv0OrEnt1'] = 1
        else:
            raise Exception("indiv0OrEnt1")

        node['noLongerListed'] = 0

        node['narrativeFileName'] = reference_number.strip() + ".shtml"

        comments1 = row['COMMENTS1']
        comments1 = comments1.replace('\n', ' ').replace('  ', ' ')

        comments1 = re.sub(' +', ' ', comments1)




        node['COMMENTS1'] = comments1.replace('"', "'").replace("INTERPOL-UN Security Council Special Notice web link:https://www.interpol.int/en/How-we-work/Notices/View-UN-Notices-Individuals", "")
        # regex = r"(Q[I|E]\..\.\d+\.\d+)" old reference number convention
        regex = r"(QD[Ii|Ee]\.\d+)"  # new reference number format
        if comments1:
            findall = re.findall(regex, comments1)

        # if reference_number == "QDe.115":
        #     print(">>>>>>>>>>>>found ", reference_number)
        if reference_number in sourceTarget.keys():
            link_list = sourceTarget[reference_number]
            # print("link list pre-existing source = ", link_list)
        else:
            link_list = []
            sourceTarget[reference_number] = link_list

        # if (len(findall) == 0):
        #     print("link_list when len(findall) == 0: ", link_list)
        #     # print(sourceTarget[reference_number])

        for other_ref_num in findall:
            # link_list = sourceTarget[reference_number]

            if other_ref_num.rstrip('.') != reference_number:
                link_list.append(other_ref_num)
                sourceTarget[reference_number] = link_list

        # if len(link_list) > 0:
        #     print("current links ", link_list)

        nationality = ''
        try:
            if 'NATIONALITY' in rowAsDict.keys():
                # if row['NATIONALITY']:
                nationality = row['NATIONALITY']
                # print(type(nationality))
                if nationality:
                    if nationality['VALUE']:
                        # print (nationality['VALUE'])
                        nationality = ",".join(nationality['VALUE'])
                else:
                    nationality = "None reported"

            if 'NATIONALITY2' in rowAsDict.keys():
                # if row['NATIONALITY2']:
                has_nat2 = True
                nat2 = row['NATIONALITY2']
                # print('NATIONALITY2 = ', nat2, ', nationality = ', nationality) 
                if len(nationality) == 0:
                    nationality = nat2
                else:
                    nationality = ",".join([nationality, nat2])       

            if len(nationality) > 0:
                node["natnlty"] = nationality
        except:
            print("Exception: nationality =", nationality )
            raise Exception("nationality")

        


        node['linksTo'] = link_list
        num_node_links = len(sourceTarget[reference_number])
        link_count_dict[reference_number] = num_node_links # len(sourceTarget[reference_number])
        node['linkCount'] = node['linkCount'] + num_node_links # + len(sourceTarget[reference_number])
        node_link_object_list = []
        for link_ref_id in link_list:
            link_object = {}
            link_object['source'] = reference_number
            link_object['target'] = link_ref_id
            node_link_object_list.append(link_object)    
            all_the_links.append(link_object)

        # if len(node_link_object_list) > 0:
        #     print('node_link_object_list = ', node_link_object_list)
        # if (links is not None and len(links) > 0):
        #     print("links = ", links)
        node['links'] = node_link_object_list
        # all_the_links.append(links)
        # if count < 13:
        #     print('all_the_links = ', all_the_links)
        total_links = total_links + num_node_links #  len(sourceTarget[reference_number])

        nodes.append(node)
        # if has_nat2:
        #     print('has_nat2 node = ', node)



for node in nodes:
    new_link_list = []
    links_to_len = len(node['linksTo'])
    # print('links_to_len = ', links_to_len)
    node_link_count = 0
    # print('node.id = ', node['id'])
    for link in all_the_links:
        # print(link['source'])
        if link['source'] == link['target']:
            raise Exception("link source == link target!!")
        if node['id'] == link['source'] or node['id'] == link['target']:
            new_link_list.append(link)
            node_link_count += 1
    node['linkCount'] = len(new_link_list) # node_link_count
    node['newLinkList'] = new_link_list
    # replacing old links value
    node['links'] = new_link_list
    # print(node['id'], " link count = ", node_link_count, " newLinkList len = ", len(node['newLinkList']))



# for node1 in nodes:
#     node1_link_count = 0
#     for node2 in nodes:
#         # if node1['id'] != node2['id']:
#         if node1['id'] in node2['linksTo']:
#             node1_link_count += 1

#     node1['linkCount2'] = node1_link_count

#     if node1['linkCount'] != node1['linkCount2']:
#         print(node1['id'], " lc1: ", node1['linkCount'], " lc2: ", node1['linkCount2'])

# links_to_len = len(node['linksTo'])
# print('links_to_len = ', links_to_len)
# node_link_count = 0
# # print('node.id = ', node['id'])
# for link in all_the_links:
#     # print(link['source'])
#     if node['id'] == link['source'] or node['id'] == link['target']:
#         node_link_count += 1
# node['linkCount'] = node_link_count
# print(node['id'], " link count = ", node_link_count)



for node in nodes[:5]:
    print('node = ', node)

data['nodes'] = nodes

print('len(all_the_links) = ', len(all_the_links))
#data['comments']['links'] = all_the_links
data['links'] = all_the_links

# print("link_count_dict = ", str(link_count_dict)[:300], ", total_links = ", total_links)
# print(count)
# print('data.keys() = ', data.keys())
all_links_1 = data['links']
print('len(all_links_1) = ', len(all_links_1))
print('al-qaida links = ', link_count_dict['QDe.115'])
# print('data.links = ', data['links'])

# COMMAND ----------

# display(link_result)

# COMMAND ----------

json.dumps(data, ensure_ascii=False)  # , ensure_ascii=False, indent=4)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls

# COMMAND ----------

import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


# COMMAND ----------

# MAGIC %sh
# MAGIC pwd
# MAGIC # ls -lahtr
# MAGIC cat /Workspace/Users/john.f.kraus19.ctr@mail.mil/data.json

# COMMAND ----------

print(sourceTarget)

# COMMAND ----------

set_of_all_links=set()
print(len(all_links_1))
print(all_links_1)
for link in all_links_1:
    linkObj = Link(link['source'], link['target']) 
    set_of_all_links.add(linkObj)
                         
print(len(set_of_all_links))   

# COMMAND ----------

indiv_sdf.show()

# COMMAND ----------

print(ent_sdf)

# COMMAND ----------

indiv_sdf.printSchema()

# COMMAND ----------

import re
count = 0
for row in indiv_coll:
    count += 1
    if count > 13:
        break;
    # print(count, row)

    print(row['FIRST_NAME'], row['SECOND_NAME'],row['THIRD_NAME'], row['FOURTH_NAME'] )
    print(row['REFERENCE_NUMBER'])
    comments1 = row['COMMENTS1']
    print(re.findall(r'(QI[.{6}])', comments1))

    # print(type(comments1))
    print(row['COMMENTS1'])

# print(count)

# COMMAND ----------

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(Q[I|E]\..\.\d+\.\d+)"

test_str = ("NASHWAN ABD AL-RAZZAQ ABD AL-BAQI None\n"
	"QI.A.12.01.\n"
	" <NAME_ORIGINAL_SCRIPT>عبد الله محمد رجب عبد الرحمن</NAME_ORIGINAL_SCRIPT>\n"
	"         <COMMENTS1>Member of Egyptian Islamic Jihad (QE.A.3.01). Review pursuant to Security Council resolution 1822 (2008) was concluded on 1 Jun. 2010.</COMMENTS1>\n"
	"         <NATIONALITY>\n"
	"            <VALUE>Egyptian</VALUE>\n"
	"         </NATIONALITY>\n"
	"[]\n"
	"ABD AL WAHAB ABD AL HAFIZ None None\n"
	"QI.A.157.04.\n"
	"[]\n"
	"ADIL MUHAMMAD MAHMUD ABD AL-KHALIQ\n"
	"QI.A.255.08.\n"
	"[]\n"
	"SAID JAN ‘ABD AL-SALAM None None\n"
	"QI.A.289.11.\n"
	"[]\n"
	"ABD ALLAH MOHAMED RAGAB ABDEL RAHMAN\n"
	"QI.A.192.05.\n"
	"[]\n"
	"MAJEED ABDUL CHAUDHRY None None\n"
	"QI.A.54.01.\n"
	"[]\n"
	"ZULKIFLI ABDUL HIR None None\n"
	"QI.A.109.03.\n"
	"[]\n"
	"DIEMAN ABDULKADIR IZZAT None None\n"
	"QI.A.200.05.\n"
	"[]\n"
	"ABDUL MANAN AGHA None None None QI.A.18.01. []\n"
	"MUHAMMAD JIBRIL ABDUL RAHMAN None\n"
	"QI.A.295.11.\n"
	"['QI.']\n"
	"ALY SOLIMAN MASSOUD ABDUL SAYED\n"
	"QI.A.229.07.\n"
	"[]\n"
	"MOHAMAD IQBAL ABDURRAHMAN None\n"
	"QI.A.86.03.\n"
	"[]\n"
	"ABDUR REHMAN None None None\n"
	"QI.A.309.12.\n"
	"[]\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.


# COMMAND ----------

indiv_coll[0]

# COMMAND ----------


