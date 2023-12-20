import os
import skills.make_and_bake_assignment as m_and_b
import skills.ark.ark_item_commands as ark
import discord
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")
bot_id = int(os.getenv("BOT_ID"))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    # Avoid looping messages
    if (message.author.id == bot_id):
        return
    
    # Check that the bot user was mentioned
    has_mention = False
    for user in message.mentions:
        if (user.id == bot_id):
            has_mention = True
            break
    if (not has_mention):
        return
        
    await m_and_b.try_execute(message)
    await ark.try_execute(message)
    
client.run(token)