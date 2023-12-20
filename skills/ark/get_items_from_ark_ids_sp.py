# https://usebeacon.app/Games/Ark/Mods/1999447172/Cheats

import json
import requests
import os
import lxml.html as html_parse

page_count = 10
page_start = 1
page_url_template = "https://usebeacon.app/Games/Ark/Mods/1999447172/Cheats/"
page_directory_path = "skills/s_temp/"
item_output_file = "skills/ark/s_items.json"

def download_item_pages():
    os.mkdir(page_directory_path)

    for i in range(page_start, page_count + 1):
        url = page_url_template + str(i)
        response = requests.get(url)
        with open(page_directory_path + f"{i}.html", "w+") as f:
            f.write(response.text)
    
def read_item_details():
    item_details = []

    for i in range(1, page_count + 1):
        root = html_parse.parse(page_directory_path + f"{i}.html").getroot()
        for tr in root.cssselect("#spawntable > tbody > tr"):
            td = tr.getchildren()
            display_name = td[0].text.strip()
            spawn_command = td[1].text.strip()
            item_details.append({
                "displayName": display_name,
                "spawnCommand": spawn_command
            })
    with open(item_output_file, "w+") as f:
        f.write(json.dumps(item_details))

download_item_pages()
read_item_details()