import os
import skills.make_and_bake_assignment as m_and_b
import skills.ark.ark_item_commands as ark
import discord
from discord import Message
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")
bot_id = int(os.getenv("BOT_ID"))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message: Message):
    # Avoid looping messages
    if message.author.id == bot_id:
        return

    # Check that the bot user was mentioned
    if not bot_id in list(map(lambda user: user.id, message.mentions)):
        return

    if "help" in message.clean_content.lower():
        await send_basic_help_message(message)
        return

    await m_and_b.try_execute(message)
    await ark.try_execute(message)


async def send_basic_help_message(message: Message):
    await message.channel.send(
        """
# Jarvis Bot Commands
1. `make and bake [participant, participant, participant]`
    * Generate make and bake assignments, create downloadable PDF of assignees
1. `item`
    * Get item spawn code for ark (enabled channels only)
"""
    )


client.run(token)
