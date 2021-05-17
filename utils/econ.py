import discord
from discord.ext import commands
import json
import os

econDB = os.path.join('json', 'econ.json')

try:
  with open(econDB) as f: # open econ database
    econ = json.load(f)  # load econ db, create callable object for it
except FileNotFoundError:
  print("Could not load json/econ.json : Ensure that the file exists, then try again. If issues persist contact the developer") # inform the user that there is an error, troubleshooting details
  econ = {} # creates temp econ dictionary for emergency use

class EconUtils():
  def __init__(self, ctx: commands.Context):
    self=self
    ctx=ctx

  def dump(filePath, dict):
    with open(filePath) as x:
      dictName = dict
      dictName = json.load(x)
    with open(filePath, 'w') as f:
      json.dump(dictName, f)
