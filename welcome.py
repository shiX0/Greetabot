import discord
import random


def image_url():
  a = random.choice(open("list.txt").readlines())
  Wurl = "https://www.memeatlas.com/" + a
  return Wurl


def embed_welcome(member):
  '''Returns embedded welcome message'''
  guild = member.guild
  embed = discord.Embed(
    title=f"𒈱Welcome To {guild}𒈱",
    description=f"{member.mention} just fell into the trap!!",
    color=0x1aff5e)
  embed.set_image(url=image_url())
  embed.set_thumbnail(
    url="https://media.tenor.com/FvthnLepGgAAAAAM/hi-hello.gif")

  embed.set_footer(text=f"current memebers:{guild.member_count}")
  return embed

def embed_bye(member):
  """returns embedded leave message"""
  guild = member.guild
  embed = discord.Embed(
    title=f"{member} vanished into dust",
    description='(left the server)',
    color=0xff0015)
  embed.set_thumbnail(
    url=member.display_avatar.url)
  embed.set_image(url="https://media.discordapp.net/attachments/863025597448978453/893874985414844496/forsenLaughingAtYou.gif")
  return embed