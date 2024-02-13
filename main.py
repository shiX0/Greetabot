import os
from keep_alive import keep_alive
import discord
import asyncio
from discord import app_commands
from welcome import embed_welcome, embed_bye
from gpt import getCompletion
from racistgpt import getrCompletion

my_secret = os.environ['botToken']
guild_id = 1012045804552339508
MY_GUILD = discord.Object(guild_id)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class MyClient(discord.Client):

  def __init__(self, *, intents: discord.Intents):
    super().__init__(intents=intents)
    self.tree = app_commands.CommandTree(self)
    self.synced = False

  async def setup_hook(self):
    # This copies the global commands over to your guild.
    self.tree.copy_global_to(guild=MY_GUILD)
    await self.tree.sync(guild=MY_GUILD)

  async def on_ready(self):
    print(f"We have logged in as {self.user}.")
    await self.change_presence(activity=discord.Game(name="with your mom"))


client = MyClient(intents=intents)


# class MyClient(discord.Client):
@client.event
async def on_member_join(member):
  guild = member.guild
  if guild.system_channel is not None:
    to_send = embed_welcome(member)
    await guild.system_channel.send(embed=to_send)


@client.event
async def on_member_remove(member):
  guild = member.guild
  if guild.system_channel is not None:
    to_send = embed_bye(member)
    await guild.system_channel.send(embed=to_send)


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$ping'):
    await message.channel.send('beep boop im still alive :pensive:')


@client.tree.command()
async def help(interaction: discord.Interaction):
  '''shows lists of all commands!'''
  await interaction.response.send_message(
    "fuck off there is no commands here sucker :middle_finger:")


@client.tree.command()
@app_commands.describe(
  prompt="A Prompt for UnhingedGPT(jailbroken text model form openai) ")
async def chat(interaction: discord.Interaction, prompt: str):
  """returns ai generated degenerate messages"""
  if len(prompt) < 200:
    try:
      await interaction.response.defer()
      message = getCompletion(message=prompt)
      await asyncio.sleep(4)
      await interaction.followup.send(
        f"{interaction.user}:{prompt}\nBot:{message}")
    except Exception:
      message = "Sorry, I didn't got that"
      await interaction.response.send_message(
      f" {interaction.user}:{prompt}\nBot:{message}")
  else:
    await interaction.response.send_message(
      "oah dud im not gonna respond to that passage!(im poor and api requests costs 🤑)"
    )


@client.tree.command()
@app_commands.describe(
  prompt="A prompt for RACIST UnhingedGPT(jailbroken text model form openai) ")
async def racechat(interaction: discord.Interaction, prompt: str):
  """returns ai generated racist and degenerate messages"""
  if len(prompt) < 200:
    try:
      await interaction.response.defer()
      message = getrCompletion(message=prompt)
      await asyncio.sleep(4)
      await interaction.followup.send(
        f"{interaction.user}:{prompt}\nBot:{message}")
    except Exception:
      message = "Sorry, I didn't got that"
      await interaction.response.send_message(f"Bot:{message}")
  else:
    await interaction.response.send_message(
      "oah dud im not gonna respond to that passage!(im poor and api requests costs 🤑)"
    )


@client.tree.context_menu(name='Show Join Date')
async def show_join_date(interaction: discord.Interaction,
                         member: discord.Member):
  # The format_dt function formats the date time into a human readable representation in the official client
  await interaction.response.send_message(
    f'{member.mention} joined at {discord.utils.format_dt(member.joined_at)}')


#
keep_alive()
client.run(my_secret)
