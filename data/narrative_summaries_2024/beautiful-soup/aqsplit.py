from bs4 import BeautifulSoup
import os

from os import listdir

my_path = '/Users/john.kraus/workspaces/aq-list-viz/data/narrative_summaries_2024/beautiful-soup/'
# ' # C:\\Python Pool\\Test'
for file_name in listdir(my_path):
    if file_name.endswith('.shtml'):
        os.remove(my_path + file_name)

# os.remove("./*.shtml")

filename = "1up29en-al-qaida.html"
with open(filename, 'r') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# span_emptyspace = soup.find_all('span', class_='emptyspace')
# print('len(span_emptyspace) = ',  len(span_emptyspace))

# for emptyless in (td for td in soup.find_all('td') if td.find('span', class_='emptyspace')):
#     print(emptyless)
#     emptyless.decompose()

# span_emptyspace.decompose()
# aq_list = soup.find_all('tr.rowtext')  # <tr class="rowtext">')

aq_list = soup.find_all("tr", class_="rowtext")

for fragment in aq_list:
    #     print(fragment.prettify())
    if fragment.find('strong') is None:
        continue
    id = fragment.find('strong').get_text()
    print('id = ', id)
    fname = id.strip() + ".shtml"
    # print(fname)
    with open(fname, 'w') as f:
        print("41 fname = ", fname)
        f.write(fragment.prettify())


    # print("------")


print(len(aq_list))
