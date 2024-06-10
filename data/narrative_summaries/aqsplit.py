from bs4 import BeautifulSoup
import os
import sys
import re

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
    # new_tag = soup.new_tag("span", class_="name")
    new_tag = soup.new_tag("span", attrs={"class": "name", "id": "doc_name"})

    # new_tag = soup.new_tag("a", attrs={"class": "classname", "href": "#", "id": "link1"})

    new_tag.string = name
    if name_element:
        name_element.replace_with(new_tag)






    name_orig_script_key_element = fragment.find('strong')
    name_orig_script_key_text = fragment.find('strong').get_text()
    print("name_orig_script_key_textX = " , name_orig_script_key_text)
    new_tag = soup.new_tag("span", class_="nameOrigScriptKey")
    new_tag.string = name_orig_script_key_text
    if (name_orig_script_key_element and "Name (original script):" in name_orig_script_key_text):
        name_orig_script_key_element.replace_with(new_tag)

    for a in fragment.find_all('a', href=True):
        a_href = a['href']
        print("Found the URL:", a['href'])
        if "https://www.interpol.int/en/How-we-work/Notices/View-UN-Notices-Entities" in a_href:
            a.decompose()
        if "click" in a.get_text():
            a.decompose()



    strongs = fragment.find_all('strong')
    for strong in strongs:
        strong_text = strong.get_text()
        if "Other information" in strong_text:
            otherInfoText = strong.next_sibling
            # print("otherInfoText = ", otherInfoText)
            otherInfoText = otherInfoText.replace('\n', ' ')
            otherInfoText = re.sub(' +', ' ', otherInfoText)
            otherInfoText = otherInfoText.replace("INTERPOL-UN Security Council Special Notice web link:https://www.interpol.int/en/How-we-work/Notices/View-UN-Notices-Individuals","")
            # new_other_info_element = soup.new_tag('span', class="otherInformationText")
            # new_tag = soup.new_tag("a", attrs={"class": "classname", "href": "#", "id": "link1"})
            new_other_info_element = soup.new_tag('span', attrs={"class": "otherInformationText", "id": "otherInfoTextId"})
            new_other_info_element.string = otherInfoText.strip()

            strong.next_sibling.replace_with(new_other_info_element)

            otherInfoText = soup.find('span', class_="otherInformationText")
            print("otherInfoText = ", otherInfoText)
            newDiv = soup.new_tag('div', attrs={"class": "moreInfoLinkDiv"})
            # newDiv.string = "Link to other info"
            # otherInfoText.insert_after(newDiv)

            strong.next_sibling.insert_after(newDiv)

            new_tag = soup.new_tag("span", class_="otherInformation")
            new_tag.string = strong_text
            strong.replace_with(new_tag)





    fragment_filename = id.strip() + ".shtml"
    # print(fname)
    with open(fragment_filename, 'w') as f:
        print("line 55 fragment_filename = ", fragment_filename)
        f.write(fragment.prettify())



    # print("------")


print(len(aq_list))
