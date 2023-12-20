import json
import requests
import os
import lxml.html as html_parse

page_count = 42
page_start = 2
first_page_url = "https://arkids.net/items"
page_url_template = "https://arkids.net/items/page/"
page_directory_path = "skills/temp/"
item_output_file = "skills/ark/items.json"

def download_item_pages():
    os.mkdir(page_directory_path)
    response = requests.get(first_page_url)
    with open(page_directory_path + "1.html", "w+") as f:
        f.write(response.text)
    
    for i in range(page_start, page_count + 1):
        response = requests.get(page_url_template + str(i))
        with open(page_directory_path + f"{i}.html", "w+") as f:
            f.write(response.text)
    
def read_item_details():
    item_details = [
        {
            "displayName": "S+ Mutator",
            "spawnCommand": "cheat GiveItem \"Blueprint'/Game/Mods/StructuresPlusMod/Misc/GenomicsChamber/PrimalItemStructure_GenomicsChamber.PrimalItemStructure_GenomicsChamber'\" 1 0 0"
        }
    ]
    for i in range(1, page_count + 1):
        root = html_parse.parse(page_directory_path + f"{i}.html").getroot()
        for tr in root.cssselect("#table > tbody > tr"):
            td = tr.getchildren()
            display_name = td[1].text_content()
            spawn_command = td[3].text_content()
            item_details.append({
                "displayName": display_name,
                "spawnCommand": spawn_command
            })
    with open(item_output_file, "w+") as f:
        f.write(json.dumps(item_details))

download_item_pages()
read_item_details()