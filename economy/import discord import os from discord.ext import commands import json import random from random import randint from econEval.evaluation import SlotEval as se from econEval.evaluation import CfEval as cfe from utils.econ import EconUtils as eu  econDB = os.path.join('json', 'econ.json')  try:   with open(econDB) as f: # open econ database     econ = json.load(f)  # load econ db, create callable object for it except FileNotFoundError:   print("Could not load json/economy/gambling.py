import discord
import os
from discord.ext import commands
import json
import random
from random import randint
from econEval.evaluation import SlotEval as se
from econEval.evaluation import CfEval as cfe
from utils.econ import EconUtils as eu

econDB = os.path.join('json', 'econ.json')

try:
  with open(econDB) as f: # open econ database
    econ = json.load(f)  # load econ db, create callable object for it
except FileNotFoundError:
  print("Could not load json/econ.json : Ensure that the file exists, then try again. If issues persist contact the developer") # inform the user that there is an error, troubleshooting details
  econ = {} # creates temp econ dictionary for emergency use

class Gambling(commands.Cog):
  def __init__(self, bot):
    self.bot=self

  #slots command
  @commands.command(name='slots', aliases=['slot', 'pennys', 'penny'])
  async def _slots(self, ctx, *, amount=None):
    id = str(ctx.author.id)
    if amount == None:
      await ctx.send("You must bet at least $100. The lack thereof is not an option.")
      return
    if id in econ:
      balance = econ[id]
      if int(amount) > balance:
        await ctx.send("You cannot bet more than you can afford")
      else:
        if int(amount) < 100:
          await ctx.send("You cannot bet less than $100")
        else:
          valOne = randint(1, 7)
          valTwo = randint(1, 7)
          valThree = randint(1, 7)
          reelOne = await se.assignValue(ctx, valOne)
          reelTwo = await se.assignValue(ctx, valTwo)
          reelThree = await se.assignValue(ctx, valThree)
          reelSum = valOne+valTwo+valThree
          embed = discord.Embed(title="Slot Machine", description="Value - {0}".format(str(reelSum)), color=discord.Colour.blurple())
          embed.add_field(name="__First Reel:__", value="{0} - {1}".format(reelOne, valOne))
          embed.add_field(name="__Second Reel:__", value="{0} - {1}".format(reelTwo, valTwo))
          embed.add_field(name='__Third Reel:__', value="{0} - {1}".format(reelThree, valThree))
          await ctx.send(embed=embed)
          if reelSum > 20:
            await ctx.send("You have hit the Jackpot!!!")
            pay = int(amount)*2
            econ[id] += pay
            eu.dump(econDB, econ)
            await ctx.send(f"Because of this, you have gained a return of ${pay}")
          elif reelSum < 21 and reelSum > 9:
            econ[id] += int(amount)
            await ctx.send(f"You won, and have earned ${amount}!")
            eu.dump(econDB, econ)
          elif reelSum < 10:
            econ[id] -= int(amount)
            await ctx.send(f"You lost, and have lost ${amount} :(")
            eu.dump(econDB, econ)
          else:
            await ctx.send("Something went wrong please try again later.")
    else:
      econ[id] = 100
      eu.dump(econDB, econ)
      balance = econ[id]
      if int(amount) > balance:
        await ctx.send("You cannot bet more than you can afford")
      else:
        if int(amount) < 100:
          await ctx.send("You cannot bet less than $100")
        else:
          valOne = randint(1, 7)
          valTwo = randint(1, 7)
          valThree = randint(1, 7)
          reelOne = se.assignValue(ctx, valOne)
          reelTwo = se.assignValue(ctx, valTwo)
          reelThree = se.assignValue(ctx, valThree)
          reelSum = valOne+valTwo+valThree
          embed = discord.Embed(title="Slot Machine", description="Value - {0}".format(str(reelSum)), color=discord.Colour.blurple())
          embed.add_field(name="__First Reel:__", value="{0} - {1}".format(reelOne, valOne))
          embed.add_field(name="__Second Reel:__", value="{0} - {1}".format(reelTwo, valTwo))
          embed.add_field(name='__Third Reel:__', value="{0} - {1}".format(reelThree, valThree))
          await ctx.send(embed=embed)
          if reelSum > 20:
            await ctx.send("You have hit the Jackpot!!!")
            pay = int(amount)*2
            econ[id] += pay
            eu.dump(econDB, econ)
            await ctx.send(f"Because of this, you have gained a return of ${pay}")
          elif reelSum < 21 and reelSum > 9:
            econ[id] += int(amount)
            await ctx.send(f"You won, and have earned ${amount}!")
            eu.dump(econDB, econ)
          elif reelSum < 10:
            econ[id] -= int(amount)
            await ctx.send(f"You lost, and have lost ${amount} :(")
            eu.dump(econDB, econ)
          else:
            await ctx.send("Something went wrong please try again later.")
  
  # cockfight command
  @commands.command(name="cockfight", aliases=['cf', 'chickenfight'])
  async def _cockfight(self, ctx, bet=None):
    id = str(ctx.author.id)
    if id in econ:
      await cfe.cfEval(ctx, ctx.author, randint(1, 2), int(bet))
      eu.Dump(econDB, econ)
    else:
      econ[id] = 100
      eu.Dump(econDB, econ)
      await cfe.cfEval(ctx, ctx.author, randint(1, 2), int(bet))
      eu.Dump(econDB, econ)
  
  # slot values
  @commands.command(name="slotvalues", aliases=['si', 'slotinfo', 'sv'])
  async def _slotvalues(self, ctx):
    n = 7 # sets the value n to 7 
    embed = discord.Embed(title="Slot Info", description="values", color=discord.Colour.blue()) # creates Embed
    while n > 0: # while n > 0, do the following
      embed.add_field(name='{0}'.format(n), value="{0}".format(await se.assignValue(ctx, n)), inline=False) # create an embed field matching the current value of n to its corresponding fruit
      n = n-1 # subtracts 1 from the current value of n
    await ctx.send(embed=embed) # sends final embed after n = 0

def setup(bot):
  bot.add_cog(Gambling(bot))
