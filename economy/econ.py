import discord
import os
from discord.ext import commands
import json
import random
from random import randint
from econEval.evaluation import Evals
from utils.econ import EconUtils as eu

# create feedback lists
workFeedback = ["You help some prisoners escape the gulag and you were awarded", "You help a child learn Russian. You were awarded", "You are forced to work in a canning factory. You earn", "Stalin asks you to be his personal bodyguard, you agreed and were awarded", "You were hired to be a guard for Lenin's tomb for a day. You are awarded.", "You work in a sweatshop making sure the children dont escape, you earned", "Your parents disown you. The state subsidizes you", "You worked as a \"Businessman\" and earned", "You work as a sex education teacher and earn", "You work as a bread line operator and earn", "You work in Gorbachev's Pizza Hut commerical and earn", "You worked and earned", "You didn't go to work, but the state still gave you"]

econDB = os.path.join('json', 'econ.json')

try:
  with open(econDB) as f: # open econ database
    econ = json.load(f)  # load econ db, create callable object for it
except FileNotFoundError:
  print("Could not load json/econ.json : Ensure that the file exists, then try again. If issues persist contact the developer") # inform the user that there is an error, troubleshooting details
  econ = {} # creates temp econ dictionary for emergency use

# create cog
class Econ(commands.Cog):
  # init func
  def __init__(self, bot):
    self.bot=self

  # work command
  @commands.command(name='work') # creates command work
  async def _work(self, ctx): # creates a few essential parameters
    if str(ctx.author.id) in econ: # checks for author id in econ
      amount = randint(1, 1000) # creates pay amount
      econ[str(ctx.author.id)] += amount # adds pay amount to author balance
      eu.dump(econDB, econ)
      message = random.choice(workFeedback) # generates random message from workFeedback list
      await ctx.send(f"{message} ${amount}") # sends feedback message
    else: # executes if author has never used the econ cog
      econ[str(ctx.author.id)] = 100 # sets author balance to default (100)
      eu.dump(econDB, econ)
      amount = randint(1, 1000)
      econ[str(ctx.author.id)] += amount
      eu.dump(econDB, econ)
      message = random.choice(workFeedback)
      await ctx.send(f"{message} ${amount}")

  # slut command
  @commands.command(name="slut")
  async def _slut(self, ctx):
    id = str(ctx.author.id)
    chance = randint(1, 4)
    amount = randint(1, 5000)
    if id in econ:
      await Evals.slut_eval(ctx, ctx.author, chance, amount) # uses slut_eval method from the Evals class, imported from econEval/evaluations
    else:
      econ[id] = 100
      eu.dump(econDB, econ)
      await Evals.slut_eval(ctx, ctx.author, chance, amount)

  #crime command
  @commands.command(name="crime")
  async def _crime(self, ctx):
    id = str(ctx.author.id)
    chance = randint(1 ,4)
    amount = randint(2, 10000)
    if id in econ:
      await Evals.crime_eval(ctx, ctx.author, chance, amount)
    else:
      econ[id] = 100
      eu.dump(econDB, econ)
      await Evals.crime_eval(ctx. ctx.author, chance, amount)

  # balance command
  @commands.command(name="bal", aliases=['balance']) # adds aliases to balance command
  async def _bal(self, ctx, member: discord.Member=None): # sets member to noe (allows us to have a predetemined member value)
    if member == None:
      member = ctx.author # sets member value to the message author is the member is not defined otherwise
    id = str(member.id)
    if id in econ:
      await ctx.send("{0}'s balance is ${1}".format(member.display_name, econ[id])) # formats in the users balance and sends it to the channel
    else:
      econ[id] = 100
      await ctx.send("{0}'s balance is ${1}".format(member.display_name, econ[id]))

  # leaderboard command
  @commands.command(name="leaderboard", aliases=['rich', 'richest', 'cucks', 'lb'])
  async def _leaderboard(self, ctx):
    top = {k: v for k, v in sorted(econ.items(), key = lambda item: item[1], reverse=True)} # create a sorted dictionary of users
    embed = discord.Embed(title="Economy Leaderboard", description="Top 5 Users", color=discord.Colour.purple()) # create embed object
    for position, user in enumerate(top): # enumerates through above dict
      member = ctx.guild.get_member(int(user)) # gets member by the id in the dict
      embed.add_field(name="{0} - {1}".format(position+1, member.mention), value="${0}".format(top[user])) # creates field of embed and value
      if position+1 > 4: # breaks if the position is greater than 5, makes sure it shows only the top 5
        break
    await ctx.send(embed=embed) # sends final embed

def setup(bot):
  bot.add_cog(Econ(bot))
