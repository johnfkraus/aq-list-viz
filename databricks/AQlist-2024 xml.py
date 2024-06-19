# Databricks notebook source
# MAGIC %md
# MAGIC ## Al Qaida sanctions list processing for D3 visualization
# MAGIC
# MAGIC Generates a JSON string to download and add to the application.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Input data: 
# MAGIC
# MAGIC /Volumes/main/default/example-data/7v9bhen-al-qaida.xml
# MAGIC
# MAGIC /Volumes/main/default/example-data/links.csv
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC tcpdump -c 5

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

# DBTITLE 1,Load XML data into Spark dataframes
# read xml file (1) individuals and (2) entities

volpath = "/Volumes/main/default/example-data/7v9bhen-al-qaida.xml"
indiv_sdf = spark.read.option("rowTag", "INDIVIDUAL").format("xml").load(volpath) 
ent_sdf = spark.read.option("rowTag", "ENTITY").format("xml").load(volpath)

# COMMAND ----------

# DBTITLE 1,Load a separately-generated CSV file contains links to narrative summaries of reasons for listing
import csv
from pyspark.sql.functions import col
# links to the summary html pages on the web; these links get added to the JSON data that drives the D3 visualization.
csv_filepath = "/Volumes/main/default/example-data/links.csv"

link_sdf = spark.read.csv(csv_filepath, header=True)
link_sdf.createOrReplaceTempView("links_table")

link_sdf.show(link_sdf.count(), False)

reference_number = 'QDi.001'
query = "SELECT link from links_table WHERE ref_num='{}'".format(reference_number)
summary_link = spark.sql(query)

print(summary_link.first()[0])

link_sdf.toPandas()

# COMMAND ----------

# MAGIC %sh
# MAGIC pip install bs4

# COMMAND ----------

import httplib2
from bs4 import BeautifulSoup, SoupStrainer

url_list = [] # looks like we don't actually use this list.
for i in link_sdf.collect():
    # display
    url_list.append(i["link"])

print(url_list)

# http = httplib2.Http()
# status, response = http.request(url_list[0])   # user agent needed to make this work
# print(response)

# for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
#     if link.has_attr('href'):
#         print(link['href'])

# COMMAND ----------


indiv_coll = indiv_sdf.collect()
print(type(indiv_coll))
print("len(indiv_coll) = ", len(indiv_coll))
ent_coll = ent_sdf.collect()
print("len(ent_coll) = ", len(ent_coll))

# COMMAND ----------

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

# test the make_link_string() method:
link_obj1 = {"source": "QDi.123", "target": "QDi.012"}
link_obj2 = {"source": "QDi.012", "target": "QDi.123"}
assert(make_link_string(link_obj1) == make_link_string(link_obj2))

# COMMAND ----------

import re
links = None
count = 0
data = {}
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
            node['DATAID'] = (row['DATAID'])
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

        if 'INDIVIDUAL_DATE_OF_BIRTH' in rowAsDict.keys():
            for dob_row in row['INDIVIDUAL_DATE_OF_BIRTH']:
                if dob_row['DATE']:
                    date_string = dob_row['DATE'].strftime("%m-%d-%Y")
                    print("date = ", dob_row['DATE'], ", date_string = ", date_string)
                    node['indiv_dob'] = date_string  

        if 'INDIVIDUAL_PLACE_OF_BIRTH' in rowAsDict.keys():
            placeOfBirth = ''
            for pob_row in row['INDIVIDUAL_PLACE_OF_BIRTH']:
                if pob_row['CITY']:
                    placeOfBirth += pob_row['CITY']
                if pob_row['STATE_PROVINCE']:
                    placeOfBirth += ", "
                    placeOfBirth += pob_row['STATE_PROVINCE']
                if pob_row['COUNTRY']:
                    placeOfBirth += ", "
                    placeOfBirth += pob_row['COUNTRY']

            node['indiv_place_of_birth'] = placeOfBirth

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
        # node['oldLinkCount'] = node['oldLinkCount'] + num_node_links # + len(sourceTarget[reference_number])
        node_link_object_list = []
        for link_ref_id in link_list:
            link_object = {}
            link_object['source'] = reference_number
            link_object['target'] = link_ref_id
            node_link_object_list.append(link_object)    
            all_the_links.append(link_object)

        node['links'] = node_link_object_list
        total_links = total_links + num_node_links #  len(sourceTarget[reference_number])
        nodes.append(node)



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
    node['oldLinkCount'] = len(new_link_list) # node_link_count
    node['newLinkList'] = new_link_list
    # replacing old links value
    node['links'] = new_link_list
    # print(node['id'], " link count = ", node_link_count, " newLinkList len = ", len(node['newLinkList']))




global_nodestring_list = []
global_link_list = []
global_linkcount = 0
for node in nodes:
    links = node['links'].copy()
    orig_len = len(links)
    # print("starting links len = ", len(links))
    nodestring_list = []
    unique_link_list = []
    for link in links:
        link_string = make_link_string(link)
        if link_string  not in nodestring_list:
            nodestring_list.append(link_string)
            unique_link_list.append(link)
        if link_string not in global_nodestring_list:
            global_nodestring_list.append(link_string)
            global_link_list.append(link)

    node['links'] = unique_link_list
    node['nodeStrings'] = nodestring_list
    # if len(new_link_list)  != orig_len:
    #     print("orig len ", orig_len, " new len ", len(new_link_list))


for node in nodes:
    node_link_count = 0
    id = node['id']
    for str in global_nodestring_list:
        if id in str:
            node_link_count += 1

    node['linkCount'] = node_link_count

# print('global_linkcount = ', global_linkcount)

data['nodes'] = nodes
data['globalLinks'] = global_link_list
data['globalLinkStrings'] = global_nodestring_list

print('len(all_the_links) = ', len(all_the_links))
#data['comments']['links'] = all_the_links
# data['links'] = all_the_links
data['links'] = global_link_list
# print("link_count_dict = ", str(link_count_dict)[:300], ", total_links = ", total_links)
# print(count)
# print('data.keys() = ', data.keys())
all_links_1 = data['links']
print('len(all_links_1) = ', len(all_links_1))
# print('al-qaida links = ', link_count_dict['QDe.115'])
# print('data.links = ', data['links'])
print("len(global_nodestring_list) = ", len(global_nodestring_list))


# COMMAND ----------

# MAGIC %md
# MAGIC ## To do: delete duplicate links from data links and data newLinkList.
# MAGIC
# MAGIC

# COMMAND ----------

def make_link_string(link):
    # print(link)
    source = link['source']
    target = link['target']
    # print("source", source, "target", target)
    nodestring = ""
    if source < target: # str(link['source']) < str(link['target']):
        nodestring = source + ","+  target #  str(link['source']) + str(link['target'])
    else:
        nodestring = target + "," + source  # str(link['target']) + str(link['source'])
    return nodestring


global_nodestring_list = []
global_link_list = []
for node in nodes:
    links = node['links'].copy()
    orig_len = len(links)
    # print("starting links len = ", len(links))
    nodestring_list = []
    new_link_list = []
    for link in links:
        link_string = make_link_string(link)
        if link_string  not in nodestring_list:
            nodestring_list.append(link_string)
            new_link_list.append(link)
        if link_string  not in global_nodestring_list:
            global_nodestring_list.append(link_string)
            global_link_list.append(link)

    node['links'] = new_link_list
    node['oldLinkCount'] = len(new_link_list)
    if len(new_link_list)  != orig_len:
        print("orig len ", orig_len, " new len ", len(new_link_list))


# COMMAND ----------

# display(link_result)

# COMMAND ----------

# copy this to local machine
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


