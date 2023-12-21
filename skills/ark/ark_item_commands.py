import json


items = None
item_lookup = []

with open("skills/ark/items.json", "r") as file:
    items = json.loads(file.read())
    item_lookup = list(enumerate(map(lambda elem: elem['displayName'].lower(), items)))

s_items = None
s_item_lookup = []

with open("skills/ark/s_items.json", "r") as file:
    s_items = json.loads(file.read())
    s_item_lookup = list(enumerate(map(lambda elem: elem['displayName'].lower(), s_items)))

item_token="item"
s_plus_token="splus"
boss_token="boss"
password_token="password"

async def try_execute(message):
    if ("ark" not in message.clean_content.lower()):
        return

    if (item_token in message.clean_content.lower()):
        await lookup_item_command(message, item_lookup, items, item_token)
        await send_command_format_reminder(message)
    elif (s_plus_token in message.clean_content.lower()):
        await lookup_item_command(message, s_item_lookup, s_items, s_plus_token)
        await send_command_format_reminder(message)
    elif (boss_token in message.clean_content.lower()):
        await boss_item_command(message)
    elif (password_token in message.clean_content.lower()):
        await send_password_command(message)
    else:
        await send_instructions(message)

async def send_command_format_reminder(message):
    await message.channel.send('\nThe three number represent quantity, quality and blueprint spawning (boolean: 0, 1) in that order.')

async def lookup_item_command(message, lookup, item_array, search_token):
    message_segments = message.clean_content.lower().split(' ')
    lookup_term_index = message_segments.index(search_token) + 1
    if (len(message_segments) <= lookup_term_index):
        await send_instructions(message)
        return

    lookup_term = " ".join(message_segments[lookup_term_index:])
    matched_item_enumerables = filter(lambda elem: lookup_term in elem[1], lookup)
    matched_item_indicides = list(map(lambda elem: elem[0], matched_item_enumerables))
    matched_items = [item_array[i] for i in matched_item_indicides]
    matched_items = matched_items[0:10]
    
    return_message = "The following items matched your search: \n\n"
    for item in matched_items:
        return_message += f"**Display Name:** {item['displayName']}\n"
        return_message += f"**Spawn Command:** {item['spawnCommand']}\n\n"
    await message.channel.send(return_message)

async def boss_item_command(message):
    return_message = "**Spawn one stack of all trophies:**\n"
    return_message += "cheat GFI Apexdrop_Allo 100 0 0;cheat GFI ApexDrop_Basilisk_Alpha 100 0 0;cheat GFI Apexdrop_AlphaCarno 100 0 0;cheat GFI Trophy_AlphaWorm 1 0 0;cheat GFI ApexDrop_CrabClaw 1 0 0;cheat GFI Apexdrop_AlphaLeeds 100 0 0;cheat GFI Apexdrop_AlphaMegalodon 100 0 0;cheat GFI Apexdrop_AlphaMosasaur 100 0 0;cheat GFI Apexdrop_AlphaRaptor 100 0 0;cheat GFI ApexDrop_ReaperBarb 100 0 0;cheat GFI Trophy_AlphaRex 1 0 0;cheat GFI Apexdrop_AlphaTuso 100 0 0;cheat GFI Apexdrop_AlphaRex 100 0 0;cheat GFI Trophy_AlphaWyvern 1 0 0;cheat GFI Apexdrop_Argentavis 100 0 0;cheat GFI ApexDrop_Basilisk 100 0 0;cheat GFI Apexdrop_Basilo 100 0 0;cheat GFI ApexDrop_CrystalWyvern 100 0 0;cheat GFI RareDrop_CorruptHeart 100 0 0;cheat GFI KeratinSpike 20 0 0;cheat GFI Apexdrop_FireWyvern 100 0 0;cheat GFI Apexdrop_Giga 100 0 0;cheat GFI Apexdrop_LightningWyvern 100 0 0;cheat GFI Apexdrop_Megalania 100 0 0;cheat GFI Apexdrop_Megalodon 100 0 0;cheat GFI Nameless 1 0 0;cheat GFI Apexdrop_PoisonWyvern 100 0 0;cheat GFI Gland 100 0 0;cheat GFI ApexDrop_RockDrake 100 0 0;cheat GFI Apexdrop_Sarco 100 0 0;cheat GFI Apexdrop_Sauro 100 0 0;cheat GFI Apexdrop_Spino 100 0 0;cheat GFI Apexdrop_Theriz 100 0 0;cheat GFI Apexdrop_Thylaco 100 0 0;cheat GFI Apexdrop_Boa 100 0 0;cheat GFI Apexdrop_Tuso 100 0 0;cheat GFI Apexdrop_Rex 100 0 0;cheat GFI Apexdrop_Yuty 100 0 0;cheat GFI Broodmother_Alpha 1 0 0;cheat GFI Dragon_Alpha 1 0 0;cheat GFI Manticore_Alpha 1 0 0;cheat GFI Gorilla_Alpha 1 0 0;cheat GFI Trophy_Rockwell_Beta_Alpha 1 0 0;cheat GFI Broodmother_Beta 1 0 0;cheat GFI Dragon_Beta 1 0 0;cheat GFI Manticore_Beta 1 0 0;cheat GFI Gorilla_Beta 1 0 0;cheat GFI Trophy_Rockwell_Beta 1 0 0;cheat GFI Broodmother_Gamma 1 0 0;cheat GFI Dragon_Gamma 1 0 0;cheat GFI Manticore_Gamma 1 0 0;cheat GFI Gorilla_Gamma 1 0 0;cheat GFI Trophy_Rockwell 1 0 0;cheat GFI King_Alpha 1 0 0;cheat GFI King_Beta 1 0 0;cheat GFI King_Gamma 1 0 0;"
    await message.channel.send(return_message)
    
    return_message = "**Spawn one of each artifact:**\n"
    return_message += "cheat GFI Artifact_12 1 0 0;cheat GFI Artifact_05 1 0 0;cheat GFI Artifact_11 1 0 0;cheat GFI Artifact_04 1 0 0;cheat GFI Artifact_07 1 0 0;cheat GFI Artifact_01 1 0 0;cheat GFI Artifact_08 1 0 0;cheat GFI Artifact_03 1 0 0;cheat GFI Artifact_02 1 0 0;cheat GFI Artifact_06 1 0 0;cheat GFI Artifact_09 1 0 0;"
    await message.channel.send(return_message)

async def send_password_command(message):
    await message.channel.send("**Enable Cheats:** EnableCheats 2Xs4sf868Y")

async def send_instructions(message):
    await message.channel.send(f"""Hmm I didn't understand that, available commands with the tagline 'ark' include
```{item_token} {{search term}}
{s_plus_token} {{search term}}
{boss_token}
{password_token}```"""
)