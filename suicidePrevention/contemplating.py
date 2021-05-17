import discord
from discord.ext import commands

class Prv():
  def __init__(self, bot):
    self.bot=self

  # creates embed object and sends it, makes things easier
  async def cont(channel, member: discord.Member):
    embed = discord.Embed(title="❤ Please give this a chance.", description="Please Listen to me....", color=discord.Colour.blurple(), url="https://www.opencounseling.com/suicide-hotlines")
    embed.add_field(name="You are important:", value="Your life is important. We all care very deeply about you. I understand that you are not happy with yourself, or you may not feel like you matter, but I can near gauruntee that you do. I know you may be reluctant, but please seek help if you are feeling this way. If it comes down to it, please call the suicide hotline, and at the very least give it a chance")
    embed.add_field(name="U.S.", value="Call (800) 273-8255 or text 'HOME' to 741741")
    embed.add_field(name="U.K.", value="Call 161-123 or text 'SHOUT' to 85258")
    embed.add_field(name="Canada", value="Call 1.833.456.4566 or text 45645")
    embed.add_field(name="Ireland", value="Call 1850 60 90 90")
    embed.add_field(name="Other Countries", value="[->click here<-](https://opencounseling.com/suicide-hotlines)")
    embed.set_footer(text="You are loved. <3 | Take these words as those from Akins, not as those from a random robot.")
    await channel.send(embed=embed)
