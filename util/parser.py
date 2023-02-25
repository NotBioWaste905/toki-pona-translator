import re

href_file = r'<a href="(.*.csv)">'

# with open("Directory Listing.html", 'r', encoding="utf-8") as f:
#     text = f.read()

# files = re.findall(href_file, text)
# with open("files.txt", 'w') as f:
#     for i in files:
#         f.write(i.split('<img src="./Directory Listing_files/text.gif" alt="[TXT]" width="16" height="16">')[0] + '\n')

import wget
import requests
# URL = 'http://antetokipona.infinityfreeapp.com/csv/archive/'
# with open("files.txt", 'r') as f:
#     files = f.read().split('\n')

# for file in files:
#     wget.download(URL+file)

a = requests.get("http://antetokipona.infinityfreeapp.com/csv/archive/tearsofsteal_vote1613642809.csv?i=1", allow_redirects=True)
with open("BLYAT.csv", 'wb') as f:
    f.write(a.content)