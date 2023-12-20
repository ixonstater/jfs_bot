
import json
from typing import List


items = None
item_lookup = []

with open("skills/ark/items.json", "r") as file:
    items = json.loads(file.read())
    item_lookup = list(enumerate(map(lambda elem: elem['displayName'].lower(), items)))


# Limit to 10 matching items
async def try_execute(message):
    # Check for ark keyword
    if ("ark" not in message.clean_content.lower()):
        return
    
    if ("lookup item" in message.clean_content.lower()):
        await lookup_item_command(message)
        await send_command_format_reminder(message)
    elif ("boss items" in message.clean_content.lower()):
        await send_command_format_reminder(message)
        # Boss item lookup
    else:
        await send_instructions(message)

async def send_command_format_reminder(message):
    await message.channel.send('The three number represent quantity, quality and blueprint spawning (boolean: 0, 1) in that order.')
    
async def lookup_item_command(message):
    message_segments = message.clean_content.lower().split(' ')
    lookup_term_index = message_segments.index('lookup') + 2
    if (len(message_segments) <= lookup_term_index):
        await send_instructions(message)
        return
    
    lookup_term = message_segments[lookup_term_index]
    matched_item_enumerables = filter(lambda elem: lookup_term in elem[1], item_lookup)
    matched_item_indicides = list(map(lambda elem: elem[0], matched_item_enumerables))
    matched_items = [items[i] for i in matched_item_indicides]
    matched_items = matched_items[0:4]
    
    return_message = "The following items matched your search: \n\n"
    for item in matched_items:
        return_message += f"**Display Name:** {item['displayName']}\n"
        return_message += f"**Spawn One:** {item['gfiCommand']}\n"
        return_message += f"**Spawn Stack:** {item['gfiCommandStack']}\n\n"
    await message.channel.send(return_message)
        

async def boss_item_command(message):
    pass

async def send_instructions(message):
    await message.channel.send("Hmm I didn't understand that, available commands with the tagline 'ark' include\n```lookup item {search term}\nboss items {map} {gamma/beta/alpha}```")