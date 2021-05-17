import discord
from discord.ext import commands
import random
import os
import json
from utils.econ import EconUtils as eu

# feedback lists
slutPos = ["The football team runs a train on you. You did a terrible job, but force them to pay your medical bills. You were *awarded*", "You shake your ass with some local russian hookers and earn", "You marry a rich old russian man, he pays you", "You commodified your body and earned", "You get it on with the attendant at the local breadline. She gives you", "You go down on the Czar's kid and earn", "You hit on one of the guard dogs at the bar, the other people nearby throw money at you out of pity. After counting you have"]

slutNeg = ["You get rammed by a guy whos bigger than a horse. You have have to pay a lot in medical bills, to be exact", "You do so terribbly that you pay your client as compensation, you lost", "You were caught having sex in a parking lot and lost", "Oops, you accidentally sucked off a member of Stalin's secret police. You are fined", "Your boyfriend finds out you have been cheating on him. He steals", "You got your dick stuck in a vacuum cleaner again. The medical bills are"]

crimePos = ["You kidnap a state official and take them hostage for", "You steal a military grade jet and sell it for", "You rob another person in the gulag for", "You rob a breadlin for", "You steal a breifcase from a strangely well dressed child. Inside of it there is", "You rob a bodybuilder for", "You steal candy from a baby worth", "You watch a mob bosses' illegal dog, you get"]

crimeNeg = ["You got caught by Stalin's secret police trying to get a free Minecraft account. You are fined", "You steal money from your neighbour. While youre running away their dog bites you and you drop the money. You must pay medical bills of", "You attempt to rob an old man, he beats you with a cane. You are forced to pay the state", "You are forced to pay a fine for jaywalking. You are lose out on", "You were caught slacking in school. You pay a fine of", "You were caught speeding. Your ticket comes out to", "You rob a bank, but you accidentally throw the money out of the window after you're startled by a gunshot through your back window. You escape the police, but you need to get your window fixed, your total comes out to"]

econDB = os.path.join('json', 'econ.json')

try:
  with open(econDB) as f: # open econ database
    econ = json.load(f)  # load econ db, create callable object for it
except FileNotFoundError:
  print("Could not load json/econ.json : Ensure that the file exists, then try again. If issues persist contact the developer") # inform the user that there is an error, troubleshooting details
  econ = {} # creates temp econ dictionary for emergency use

class Evals():
  def __init__(self, ctx: commands.Context):
    self=self
    ctx = ctx
  
  #slut chance eval
  async def slut_eval(channel, user: discord.Member, chance: int, amount: int): # takes in input of the member, chance, and amount
    id = str(user.id) # defines user id
    if chance == 1: # creates a 25% chance of loss
      econ[id] -= amount
      eu.dump(econDB, econ)
      message = random.choice(slutNeg)
      await channel.send(f"{message} ${amount}")
    else: # creates a 75% chance of success
      econ[id] += amount
      eu.dump(econDB, econ)
      message = random.choice(slutPos)
      await channel.send(f"{message} ${amount}")

    # crime chance eval
    async def crime_eval(channel, user: discord.Member, chance: int, amount: int): # takes in input of the member, chance, and amount
      id = str(user.id) # defines user id
      if chance == 1: # creates a 25% chance of success
        econ[id] += amount
        eu.dump(econDB, econ)
        message = random.choice(crimePos)
        await channel.send(f"{message} ${amount}")
      else: # creates a 75% chance of loss
        econ[id] -= amount
        eu.dump(econDB, econ)
        message = random.choice(crimeNeg)
        await channel.send(f"{message} ${amount}")

class SlotEval():
  def __init__(self, ctx: commands.Context):
    self=self
    ctx=ctx

  # assigns an emoji to a slot value
  async def assignValue(channel, value: int):
    if value == 1:
      f = '🍌'
      return f
    if value == 2:
      f = '🍒'
      return f
    if value == 3:
      f = '🍉'
      return f
    if value == 4:
      f = '🍎'
      return f
    if value == 5:
      f = '🍓'
      return f
    if value == 6:
      f = '🥭'
      return f
    if value == 7:
      f = '🥝'
      return f
    elif value > 7:
      await channel.send("Error: Incorrect use of assignValue function. Inputted values must be between 1 and 7")
      return 0

class CfEval():
  def __init__(self, ctx: commands.Context):
    self = self
    ctx = ctx

  async def cfEval(channel, user: discord.Member, chance: int, bet: int):
    id = str(user.id)
    if bet > econ[id]:
      await channel.send("You cannot make this bet as you do not have enough money.")
      return
    if bet < 100:
      await channel.send("Your bet must be larger than $100")
      return
    if chance == 1:
      econ[id] += bet
      eu.dump(econDB, econ)
      await channel.send(f"Your chicken won, and earned you {bet}")
    else:
      econ[id] -= bet
      eu.dump(econDB, econ)
      await channel.send(f"Your chicken lost and has likewise lost you ${bet}, what a dissapointment.")
