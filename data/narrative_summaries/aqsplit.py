from bs4 import BeautifulSoup
import os
import sys

from os import listdir

my_path = '/Users/john.kraus/workspaces/aq-list-viz/data/narrative_summaries/'
# ' # C:\\Python Pool\\Test'
for file_name in listdir(my_path):
    if file_name.endswith('.shtml'):
        os.remove(my_path + file_name)

# os.remove("./*.shtml")

filename = "1up29en-al-qaida.html"
with open(filename, 'r') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

span_emptyspace = soup.find_all('span', class_='emptyspace')
print('len(span_emptyspace) = ',  len(span_emptyspace))
for span in span_emptyspace:
    span.decompose()

span_emptyspace = soup.find_all('span', class_='emptyspace')
print('len(span_emptyspace) = ',  len(span_emptyspace))

# sys.exit()

aq_list = soup.find_all("tr", class_="rowtext")

for fragment in aq_list:
    #     print(fragment.prettify())
    if fragment.find('strong') is None:
        continue
    # convert strong into span
    # get id for file naming
    id_element = fragment.find('strong')
    id = fragment.find('strong').get_text()
    new_tag = soup.new_tag("span", class_="id")
    new_tag.string = id
    if id_element:
        id_element.replace_with(new_tag)
    print('id = ', id)

    # strong name to span
    name_element = fragment.find('strong')
    name = fragment.find('strong').get_text()
    new_tag = soup.new_tag("span", class_="name")
    new_tag.string = name
    if name_element:
        name_element.replace_with(new_tag)




    fragment_filename = id.strip() + ".shtml"
    # print(fname)
    with open(fragment_filename, 'w') as f:
        print("line 55 fragment_filename = ", fragment_filename)
        f.write(fragment.prettify())


    # print("------")


print(len(aq_list))
