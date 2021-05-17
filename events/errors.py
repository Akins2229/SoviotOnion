# import essential modules
import discord
from discord.ext import commands

# create Class (as Cog)
class ErrorHandling(commands.Cog):
  # init func
  def __init__(self, bot):
    self.bot=self

  # error hadnling event
  @commands.Cog.listener() # creates Event listener
  async def on_command_error(self, ctx, error): # checks for error, gets message context, initializes event as part of class
    await ctx.send(f"```Bot has run into an issue:\n {error}```") # sends error

# add cog (in setup function as per DiscordPy documentation)
def setup(bot): # include bot object in setup function
  bot.add_cog(ErrorHandling(bot)) # adds cog (Note: I will not be going into this much detail in further cogs)
