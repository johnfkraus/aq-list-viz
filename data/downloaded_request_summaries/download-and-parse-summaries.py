# download summary files, parse out selected content, write to files.
# from urllib.request import urlretrieve
import requests
import csv
# import os
from bs4 import BeautifulSoup
import sys
import re
# https://realpython.com/python-download-file-from-url/

# todo: remove all <p>&nbsp</p>
# give each field label an id so they can be styled separately
# give each div class="field-items" an id so they can be styled separately
# if local script name == name, delete local script name.
# parse all the summary files to extract additional links, add the links to the json.
# add search by nationality
# add fields from json: DOB, etc.
# increase graph window size; more scrolling

with open('summary-links.csv', newline='') as f:
    reader = csv.reader(f)
    link_data = list(reader)

print(link_data[1:4])

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

for row in link_data:
    ref_num = row[0]
    # skip header row
    if ref_num == "ref_num":
        continue
    # the URL is in the third column
    url = row[2]

    filename = ref_num + ".shtml"
    print("filename = ", filename)
    print("summary page url = ", url)
    response = requests.get(url, headers=headers)  # , params=query_parameters)
    # print(response.headers)
    # print("response_url = ", response.url)
    # print("response.status_code = ", response.status_code)
    # print("response.text = ", response.text)

    soup = BeautifulSoup(response.text, 'html.parser')

    # nonBreakSpace = u'\xa0'
    # soup = soup.replace(nonBreakSpace, ' ')

    header_elements = soup.find_all('header')
    for header in header_elements:
        soup.find('header').decompose() # .replace_with(t)

    divFieldReasonForListingOuter = soup.find("div", {"class": "field-name-field-reason-for-listing"})
    # print(divFieldReasonForListingOuter)
    for div1 in divFieldReasonForListingOuter.find_all("div"):  # ,{"class": "field-items"})
        div2 = div1.find("div")
        print(div2)

        # new_tag.string = txt
        # divFieldLabel.replace_with(new_tag)
        # txt = divFieldReasonForListingOuter.text
        # if "Reason for listing" in txt:
        #     new_tag = soup.new_tag("div", attrs={"class": "field-label", "id": "reasonForListing"})
        #     new_tag.string = txt
        #     divFieldLabel.replace_with(new_tag)




    # create id for div.field-name
    for divFieldLabel in soup.findAll("div", {"class": "field-label"}):
        txt = divFieldLabel.text
        if "Reason for listing" in txt:
            new_tag = soup.new_tag("div", attrs={"class": "field-label", "id": "reasonForListing"})
            new_tag.string = txt
            divFieldLabel.replace_with(new_tag)

    # fieldNames = soup.find_all('div', class_="field-name")
    # for fieldName in fieldNames:
    #     txt = fieldName.text

    # soup.find('strong').replace_with(t)

    # new_tag = soup.new_tag("span", attrs={"class": "name", "id": "doc_name"})

    # new_tag = soup.new_tag("a", attrs={"class": "classname", "href": "#", "id": "link1"})

    # new_tag.string = name
    # if name_element:
    #     name_element.replace_with(new_tag)

    if soup.find('span', class_="submitted"): # .decompose()
        soup.find('span', class_="submitted").decompose()
    if soup.find('footer'):  # .decompose()
        soup.find('footer').decompose()

    if soup.find('div', class_="field-name-field-reference-number"):  # .decompose()
        soup.find('div', class_="field-name-field-reference-number").decompose()

    claz = "field-name-field-name"
    if soup.find('div', class_=claz):  # .decompose()
        soup.find('div', class_= claz).decompose()

    claz = "field-name-field-legal-basis"
    if soup.find('div', class_=claz):  # .decompose()
        soup.find('div', class_= claz).decompose()

    claz = "field-name-field-posted-on"
    if soup.find('div', class_=claz):  # .decompose()
        soup.find('div', class_= claz).decompose()

    claz = "field-name-field-updated-on"
    if soup.find('div', class_=claz):  # .decompose()
        soup.find('div', class_= claz).decompose()

    strongs = soup.find_all('strong')
    for strong in strongs:
        t = strong.text
        soup.find('strong').replace_with(t)

    # addtl_info = soup.find('div', class_="field-name-field-additional-information").prettify()
    region_content = soup.find('div', class_="region-content").prettify()

    region_content_str = str(region_content)
    # region_content_str = region_content_str.replace('\n', ' ')
    # region_content_str =  re.sub(' +', ' ', region_content_str)

    print("region_content_str = ", region_content_str)
    # exit()

    filepath = "/Users/john.kraus/workspaces/aq-list-viz/data/downloaded_request_summaries/" + filename
    with open(filepath, mode="w") as file:
        file.write(region_content_str)
        file.close()
