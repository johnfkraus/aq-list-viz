
from urllib.request import urlretrieve
import requests
import csv
import os
from bs4 import BeautifulSoup
import sys
import re


# https://realpython.com/python-download-file-from-url/


with open('summary-links.csv', newline='') as f:
    reader = csv.reader(f)
    link_data = list(reader)

print(link_data[1:4])

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# result = requests.get(url, headers=headers)


for row in link_data:
    # row = link_data[1]
    ref_num = row[0]
    if ref_num == "ref_num":
        continue
    url = row[2]
    # exit()

    filename = ref_num + ".html"
    print("filename = ", filename)

    # # urlretrieve(url, filename)
    #
    # # ('gdp_by_country.zip', <http.client.HTTPMessage object at 0x7f06ee7527d0>)
    # # path, headers = urlretrieve(url, filename)
    # # urls = ["https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD",   "https://www.un.org/securitycouncil/content/sultan-aziz-azam"]
    # urls = ["https://www.un.org/securitycouncil/content/sultan-aziz-azam"]

    # query_parameters = {"downloadformat": "csv"}


    # for url in urls:
    print("url = ", url)
    response = requests.get(url, headers=headers)  # , params=query_parameters)
    # print(response.headers)
    # print("response_url = ", response.url)
    # print("response.status_code = ", response.status_code)
    # print("response.text = ", response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
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


    # region_content.find('span', class_="submitted").decompose()
    # region_content.submitted.decompose()


    print(region_content)
    # exit()

    # node-1461 > div.field.field-name-field-additional-information.field-type-text-long.field-label-above




    # for k in response.headers.keys(): # .items():
    #      print(k, ": ", response.headers[k])
    filepath = "/Users/john.kraus/workspaces/aq-list-viz/data/downloaded_request_summaries/" + filename
    # with open("/Users/john.kraus/workspaces/aq-list-viz/data/downloaded_request_summaries/testfile.html", mode="w") as file:
    with open(filepath, mode="w") as file:
        file.write(str(region_content))
        file.close()

