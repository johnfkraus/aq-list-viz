import httplib2

from bs4 import BeautifulSoup, SoupStrainer

# url_list = []
# for i in link_sdf.collect():
#     # display
#     # print(i["link"])  # , i["NAME"], i["Company"])
#     url_list.append(i["link"])

print(summary_urls[0])

# http = httplib2.Http()
# status, response = http.request(url_list[0])
# print(response)
#
# for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
#     if link.has_attr('href'):
#         print(link['href'])
