# create list of reference numbers and links from html tables in HTML pages; save as CSV file.
from bs4 import BeautifulSoup
import os
import sys
import csv
from os import listdir

# my_path = '/Users/john.kraus/workspaces/aq-list-viz/data/narrative_summaries_2/'

# list of manually downloaded pages containing links to summaries
filenames = ["01-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html",
             "02-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html",
             "03-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html",
             "04-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html",
             "05-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html",
             "06-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html",
             "07-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html",
             "08-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html",
             "09-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html",
             "10-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html",
             "11-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html",
             "12-Narrative Summaries of Reasons for Listing _ United Nations Security Council.html"
             ]

# for file_name in listdir(my_path):
#     if file_name.endswith('.csv'):
#         os.remove(my_path + file_name)


csv_header = ["ref_num", "name", "link", "posted_on"]

# with open('links.csv', 'a', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',',
#                             quotechar='"', quoting=csv.QUOTE_ALL)
#     writer.writerow(csv_header)  # ['Spam'] * 5 + ['Baked Beans'])

trow_count = 0
for filename in filenames:
    # filename = filenames[0]  # "1up29en-al-qaida.html"
    with open(filename, 'r') as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.find('table')
    tbody = table.find('tbody')
    trows = tbody.find_all('tr')
    print("filename: ", filename, " has #trows = ", len(trows))
    # print("len(trows) = ", len(trows))
    trow_count += len(trows)
    for row in trows:
        try:
            ref_num = row.find('td', class_="views-field-field-reference-number").get_text().strip()

            print("starts with: ", ref_num)
        except:
            print("filename = ", filename)
            print("row = ", row, " END OF ROW")
            print("row.find ... = ", row.find('td', class_="views-field-field-reference-number")) # .get_text().strip()
            raise Exception("NoneType has no attribute get_text")

        break

print("trow_count = ", trow_count)


        # td_name_link = row.find('td', class_="views-field-title")
        # td_name_link_a = td_name_link.find('a')
        # link = td_name_link_a['href'].strip()
        # print(link)
        #
        # # class ="views-field views-field-title" >
        # # name = row.find('span', class_="ltr").get_text().strip()
        # # print(name)
        # name = td_name_link_a.find('span').get_text().strip()
        # print(name)
        #
        # posted_on = row.find('span', class_="date-display-single").get_text().strip()
        # print(posted_on)
        #
        # csv_row = [ref_num, name, link, posted_on]
        # # csv_row.append(ref_num)
        # # csv_row.append(name)
        # # csv_row.append(link)
        # # csv_row.append(posted_on)
        # print("csv_row = ", csv_row)
        #
        # with open('links.csv', 'a', newline='') as csvfile:
        #     writer = csv.writer(csvfile, delimiter=',',
        #                             quotechar='"', quoting=csv.QUOTE_ALL)
        #     writer.writerow(csv_row)  # ['Spam'] * 5 + ['Baked Beans'])
        #     # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
        #
        # # class ="date-display-single" > 07 April 2011 < / span >
        #
