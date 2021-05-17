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

@bot.group(invoke_without_command=True)
async def help(ctx):
  embed=discord.Embed(title="Help Command")
  embed.add_field(name="Music", value="Category for Music Commands", inline=False)
  embed.add_field(name="Moderation", value="Category for Moderation Commands", inline=False)
  embed.add_field(name="Fun", value="Category for Fun Commands", inline=False)
  embed.add_field(name="Economy", value="Category for Economy Commands", inline=False)
  embed.add_field(name="Gambling", value="Category for Gambling Commands", inline=False)
  await ctx.send(embed=embed)

@help.command()
async def economy(ctx):
  embed=discord.Embed(title="Economy Help Command", color=0xfeadad)
  embed.add_field(name="Work", value="You will work for money; Usage: {prefix}work", inline=False)
  embed.add_field(name="Slut", value="You will do something slutty for money; Usage:{prefix}slut", inline=False)
  embed.add_field(name="Crime", value="You will commit a crime for money; Usage:{prefix}crime", inline=False)
  embed.add_field(name="Balance", value="Ascertains a members balance; Usage:{prefix}balance {member: optional}", inline=False)
  embed.add_field(name="Leaderboard", value="Displays the top 5 richest members; Usage:{prefix}leaderboard", inline=False)
  await ctx.send(embed=embed)

@help.command()
async def music(ctx):
  embed=discord.Embed(title="Music Help Command")
  embed.add_field(name="Play", value="Will play a given video; Usage:{prefix}play {song}", inline=False)
  embed.add_field(name="Now", value="Will display the currently playing video; Usage:{prefix}now", inline=False)
  embed.add_field(name="Queue", value="Will display the next 10 videos; Usage:{prefix}queue {page: optional}", inline=False)
  embed.add_field(name="Skip", value="Will skip the currently playing song; Usage:{prefix}skip", inline=False)
  embed.add_field(name="Remove", value="Will remove a song from the queue; Usage:{prefix}remove {song number}", inline=False)
  embed.add_field(name="Stop", value="Will stop the current song, clear the queue, and leave the channel; Usage:{prefix}stop", inline=False)
  embed.add_field(name="Pause", value="Will pause the current song; Usage:{prefix}pause", inline=False)
  embed.add_field(name="Resume", value="Will resume the current song (if paused); Usage:{prefix}resume", inline=False)
  embed.add_field(name="Volume", value="Will change the current volume of the bot; Usage:{prefix}volume {int: 1-100}", inline=False)
  embed.add_field(name="Join", value="Will have the bot join your current voice channel; Usage:{prefix}join", inline=False)
  await ctx.send(embed=embed)

@help.command()
async def gambling(ctx):
  embed=discord.Embed(title="Gambling Help Command")
  embed.add_field(name="Slots", value="Will have you bet on the slot machine; Usage:{prefix}slots {bet: int>100}", inline=False)
  embed.add_field(name="Cockfight", value="Will have you bet on a cockfight; Usage:{prefix}cockfight {bet: int>100}", inline=False)
  await ctx.send(embed=embed)

@help.command()
async def fun(ctx):
  embed=discord.Embed(title="Fun Help Command")
  embed.add_field(name="badtake", value="Displays one of many badtakes that I have; Usage:{prefix}badtake", inline=False)
  embed.add_field(name="acab", value="Displays my opinion on ACAB; Usage:{prefix}acab", inline=True)
  embed.add_field(name="blm", value="Displays my opinion of BLM; Usage:{prefix}blm", inline=True)
  embed.add_field(name="Respect", value="Will ascertain whether or not I respect something; Usage:{prefix}respect {argument}", inline=True)
  embed.add_field(name="Say", value="Will have the bot say something; Usage:{prefix}say {message}", inline=True)
  embed.add_field(name="Anarkiddy", value="Anarchists are cringe, the voices of the heavens above (myself) will tell you such; Usage:{prefix}anarkiddy", inline=True)
  embed.add_field(name="Google", value="Will google something; Usage:{prefix}google \"{query}\" {limit: int (Optional)}", inline=True)
  embed.add_field(name="Define", value="Will define a given word; Usage:{prefix}define {word}", inline=True)
  embed.add_field(name="Translate", value="Will translate a given word to English; Usage:{prefix}translate {word}", inline=True)
  embed.add_field(name="Translatedefine", value="Will define a word from another language; Usage:{prefix}translatedefine {word}", inline=True)
  embed.add_field(name="Level", value="Will give you the member of a member; Usage:{prefix}level {member: optional}", inline=True)
  embed.add_field(name="Levels", value="Will display the 5 highest levels; Usage:{prefix}levels", inline=True)
  embed.add_field(name="Transgender", value="Voices my opinion on Trans Rights; Usage:{prefix}transgender", inline=True)
  embed.add_field(name="Thesaurus", value="Will display synonyms and antonyms for a given word; Usage:{prefix}thesaurus {word{", inline=True)
  embed.set_footer(text="Note: Any and all words spoken by this bot, from any commands in this cog are not liable to Akins")
  await ctx.send(embed=embed)

@help.command()
async def moderation(ctx):
  embed=discord.Embed()
  embed.add_field(name="Ban", value="Will ban a user; Usage:{prefix}ban {member} {reason: optional}}", inline=False)
  embed.add_field(name="Kick", value="Will kick a user; Usage:{prefix}kick {member} {reason: optional}", inline=True)
  embed.add_field(name="Mute", value="Will mute a user; Usage:{prefix}mute {member} {duration: minutes} {reason: optional}", inline=True)
  embed.add_field(name="Unmute", value="Will unmute a user; Usage:{prefix}unmute {member}", inline=True)
  embed.add_field(name="Hackban", value="Will ban, then unban a user; Usage:{prefix}hackban {member} {reason: optional}", inline=True)
  embed.add_field(name="Softban", value="Will ban a user for a given time; Usage:{prefix}softban {member} {duration: minutes} {reason: optional}", inline=True)
  embed.add_field(name="Unban", value="Will unban a user; Usage:{prefix}unban {member}", inline=True)
  embed.add_field(name="Userinfo", value="Will give information on a user; Usage:{prefix}userinfo {member: optional}", inline=True)
  embed.add_field(name="Avatar", value="Will display a users avatar; Usage:{prefix}avatar {member: optional}", inline=True)
  embed.add_field(name="Purge", value="Will purge a given number of messages; Usage:{prefix}purge {limit: int}", inline=True)
  embed.set_footer(text="All of these commands require their respective permissions")
  await ctx.send(embed=embed)

# load cogs & run bot
if __name__ == '__main__':
  for cog in cogs:
    bot.load_extension(cog) # loads cog to bot
  run() # runs bot
  while True:
    on = True
