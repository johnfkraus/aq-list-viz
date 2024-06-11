
from urllib.request import urlretrieve
import requests
import csv
import os

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
    print("response.content = ", response.text)

    # for k in response.headers.keys(): # .items():
    #      print(k, ": ", response.headers[k])
    filepath = "/Users/john.kraus/workspaces/aq-list-viz/data/downloaded_request_summaries/" + filename
    # with open("/Users/john.kraus/workspaces/aq-list-viz/data/downloaded_request_summaries/testfile.html", mode="w") as file:
    with open(filepath, mode="w") as file:
        file.write(str(response.text))
        file.close()
