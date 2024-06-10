# create list of reference numbers and links from html tables in HTML pages.
from bs4 import BeautifulSoup
import os
import sys
import csv
from os import listdir

my_path = '/Users/john.kraus/workspaces/aq-list-viz/data/narrative_summaries_2/'

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

for file_name in listdir(my_path):
    if file_name.endswith('.csv'):
        os.remove(my_path + file_name)


csv_header = ["ref_num", "name", "link", "posted_on"]

with open('links.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(csv_header)  # ['Spam'] * 5 + ['Baked Beans'])


for filename in filenames:
    # filename = filenames[0]  # "1up29en-al-qaida.html"
    with open(filename, 'r') as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    table = soup.find('table')
    tbody = table.find('tbody')
    trows = tbody.find_all('tr')
    print(len(trows))

    for row in trows:
        ref_num = row.find('td', class_="views-field views-field-field-reference-number").get_text().strip()
        print(ref_num)

        td_name_link = row.find('td', class_="views-field-title")
        td_name_link_a = td_name_link.find('a')
        link = td_name_link_a['href'].strip()
        print(link)

        # class ="views-field views-field-title" >
        # name = row.find('span', class_="ltr").get_text().strip()
        # print(name)
        name = td_name_link_a.find('span').get_text().strip()
        print(name)

        posted_on = row.find('span', class_="date-display-single").get_text().strip()
        print(posted_on)

        csv_row = [ref_num, name, link, posted_on]
        # csv_row.append(ref_num)
        # csv_row.append(name)
        # csv_row.append(link)
        # csv_row.append(posted_on)
        print(csv_row)

        with open('links.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(csv_row)  # ['Spam'] * 5 + ['Baked Beans'])
            # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

        # class ="date-display-single" > 07 April 2011 < / span >

sys.exit()

span_emptyspace = soup.find_all('span', class_='emptyspace')
print('len(span_emptyspace) = ', len(span_emptyspace))
for span in span_emptyspace:
    span.decompose()

span_emptyspace = soup.find_all('span', class_='emptyspace')
print('len(span_emptyspace) = ', len(span_emptyspace))

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
