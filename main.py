"""
# Copyright Notice

Copyright M. Akins 2021

# Licensing

M.I.T License

# Terms of Service

Any and all use of this program is allowed, however any malicous use, or changes made to or of the program are not the responsibility of Akins

# Developer Contact

If you have any issues at all contact me on Discord at Akins#2229, or by email at akins2229@gmail.com
"""

# import essential modules
import discord
from discord.ext import commands
import os
import json
from suicidePrevention.contemplating import Prv as pr

# create keyword list
keywords = ['kill myself', 'suicide', 'kms', 'kys', 'want to die', 'wanna die', 'jump off a bridge', 'Suicide', 'Kill myself', 'Kill Myself', 'Kms', 'KMS']

# input startup information
prefix = input("Define the bot prefix on startup\n")

# get bot token
tokenText = os.path.join('', 'token.txt')
with open(tokenText) as f:
  token = f.read()

# construct bot
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), help_command=None)

# cogs list
cogs = ['economy.econ', 'events.errors', 'economy.gambling', 'misc.music', 'misc.fun', 'misc.moderation']

# bot run function
def run():
  bot.run(token)

# on_ready event
@bot.event
async def on_ready():
  print("---------------------------")
  print("STATUS - ONLINE\nUSERNAME - {0}\nID - {1}\nDEVELOPER - AKINS\nVERSION - 4.0.2".format(bot.user, bot.user.id)) # prints things when the bot is onlines
  print("---------------------------")

# checks for keywords
@bot.event # creates Event Listener
async def on_message(message):
  if message.author.id == bot.user.id:
    await bot.process_commands(message)
    pass
  else:
    for keyword in keywords:
      if keyword in message.content:
        await message.channel.send("You mentioned word {0}, this is a word related to suicide".format(keyword))
        await pr.cont(message.channel, message.author)
      else:
        pass
    if message.author.bot == False:
        with open('json/users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)
  await bot.process_commands(message)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
	experience = users[f'{user.id}']['experience']
	lvl_start = users[f'{user.id}']['level']
	channel = bot.get_channel(832655762089181204)
	lvl_end = int(experience ** (1 / 4))
	if lvl_start < lvl_end:
		await channel.send(f'{user.mention} has leveled up to level {lvl_end}')
		users[f'{user.id}']['level'] = lvl_end

@bot.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('json/users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'You are at level {lvl}!')
    else:
        id = member.id
        with open('json/users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'{member} is at level {lvl}!')

			
@bot.command()
async def levels(ctx):
	embed = discord.Embed(title="☭SOVIOT ONION☭ Levels Leaderboard", color=discord.Colour.green())
	with open('json/users.json', 'r') as file:
		data = json.load(file)
	sorted_data = {id: bal for id, bal in sorted(data.items(), key=lambda item: item[1]['level'], reverse=True)}
	for pos, (id, bal) in enumerate(sorted_data.items()):
		member = ctx.guild.get_member(int(id))
		strBal = str(bal)
		firstStr = strBal.replace("}", "")
		secStr = firstStr.replace("{", "")
		thrStr = secStr.replace("'", "")
		embed.add_field(name=f"{pos+1} - {member.name}", value=f"{thrStr}", inline=False)
		if pos+1 > 4:
			break 
	await ctx.send(embed=embed)	

# load cogs & run bot
if __name__ == '__main__':
  for cog in cogs:
    bot.load_extension(cog) # loads cog to bot
  run() # runs bot
  while True:
    on = True
