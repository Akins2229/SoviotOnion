import discord
from discord.ext import commands
import random
from time import strftime, localtime
import random
from random import randint
from PyDictionary import PyDictionary

botDict = PyDictionary()

marmname = ['Marma', 'marma', 'marm', "Marm"]
list = ["The Katyn Massacre didnt happen, seethe liberal", "Katyn didn't happen, they were just lying about the records of over 20,000 deaths", "Stalin didn't hate jews, look at all these quotes where he said he didn't ~~ignore the fact that he also said he hated them multiple times~~", "The NVKD massacre didnt happen, its just CIA propaganada you western imperialist...", "The Holodomor didnt happen, the Kulaks just burned the grain", "Anarchy doesnt work idiot wetsern imperialist", "ABORTION IS MURDER!!! IF DADDY STALIN DOESNT HAVE ALL OF THE BABIES TO MURDER THEN I DONT WANT IT TO HAPPEN", "If its illegal its wrong. Legality = Ethicality, Legality = Morality", "Stalin didnt have secret police youre just a libtard", "STOP NARRATING CHESS YOU BRITISH CUCK @comrade.noble#1213", "Trans people dont exist, they are not valid because I, SOVIOT ONION, said so.", "*misgenders the nearest trans person*", "Dugs are not a commodity, they are my means of production, of course I am producing unskilled labourers who I can mold to my image to serve myself and Stalin", "The object of egality is in all form the only means of determining morality. If you do something illegal, you are thrown into the gulag for being immoral, is a simple system", "There is nothing wrong with the gulags, or with exile. After all, you can have all the freedom you want in Siberia.", "Serbia is based", "Those who do not work are a leech, and shold be made to by the utmost force", "\"Empathize with someones reasons not to do something\", empathize with what? How much your feet hurt? People who are in pain should work regardless, I dont care if youre being burned alive, state production waits for no lazy idiot.", "Katyn didn't happen, I dont know about it so it can't have been real", "Ayn Rand isn't that badddd.", "Transgenderism doesn't matter to me. It isn't revolutionary for my specific cause", "No amount of empathizing with the working class will get my state up and running.", "Equitability for the working class? Comrade, you work until you die, and then work some more.", "Not everyone deserves to eat, some people aren't worthy to such a cause", "The only way you leave my socialist state is with the sweet release of death.", "There are many people who do not deserve to live. Ex: Prisoners, Religious people etc.", "Stuttering is just your brain telling you to put your blood sweat and tears into the state.", "He who disagrees with me is just an apparatus of the bourgeoisie."]

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="badtake")
	async def _badtake(self, ctx):
		take = random.choice(list)
		await ctx.send(take)

	@commands.command(name="respect")
	async def _respect(self, ctx, *, msg):
		num = randint(1, 21)
		if num == 20:
			await ctx.send(f"**Yes**, I will respect {msg} comrade!")
		else:
			await ctx.send(f"No, I will not respect {msg} liberal")

			
	@commands.command(name='say')
	async def _say(self, ctx, *, message):
		await ctx.message.delete()
		await ctx.send(message)
		print(f"{ctx.message.author} - {message}" + strftime("%Y-%m-%d %H:%M:%S", localtime()))

	@commands.command(name="anarkiddy")
	async def _anarkiddy(self, ctx):
		await ctx.send(f"{ctx.message.author.mention} - seethe idiot anarkiddie cope libtard")

	@commands.command(name="acab")
	async def _acab(self, ctx):
		await ctx.send("WTF DID YOU JUST SAY YOU IDIOT THE POLICE ARE BASED AND DOM ME NIGHTLY")

	@commands.command(name='blm')
	async def _blm(self, ctx):
		await ctx.send("My support for black liberation is conditional as to whether or not it helps the state run means of production")

	@commands.command(name='transgender')
	async def _transgender(self, ctx):
		await ctx.send(f"Transgenders don't help my revolution, I couldnt give a damn less about their so called dysphoria. If anything they're just gays who are unwilling to admit it.")

	@commands.command(name="define")
	async def _define(self, ctx, *, word):
		if word in marmname:
			await ctx.send(f"{word} - A sexy hot sexy motherfucker who makes me want to cum")
		else:
			text = botDict.meaning(word)
			txt = str(text)
			firstStr = txt.replace('{', "")
			secondStr = firstStr.replace("}", "")
			thirdStr = secondStr.replace("'", "")
			fourthStr = thirdStr.replace("]", "")
			finalStr = fourthStr.replace("[", "")
			await ctx.send(finalStr)
		
	@commands.command(name="translate")
	async def _translate(self, ctx, *, word):
		text = botDict.translate(word,'en')
		await ctx.send(text)
		
	@commands.command(name='translatedefine')
	async def _translatedefine(self, ctx, *, word):
		text = botDict.translate(word,'en')
		txt = botDict.meaning(text)
		textf = str(txt)
		firstStr = textf.replace('{', "")
		secondStr = firstStr.replace("}", "")
		thirdStr = secondStr.replace("'", "")
		fourthStr = thirdStr.replace("]", "")
		finalStr = fourthStr.replace("[", "")
		await ctx.send(finalStr)
		
	@commands.command(name="thesaurus")
	async def _thesaurus(self, ctx, *, word):
		syn = botDict.synonym(word)
		ant = botDict.antonym(word)
		embed = discord.Embed(title=word, description="Word Thesaurus", color=0xfeadad)
		embed.add_field(name="Synonyms:", value=syn)
		embed.add_field(name="Antonyms:", value=ant)
		await ctx.send(embed=embed)
		
	@commands.command(name="google")
	async def _google(self, ctx, term, length=None):
		if length == None:
			length = '1'
		embed = discord.Embed(title="Google Search", description=f"Search for {term}", color=0xfeadad)
		intLength = int(length)
		try:
			from googlesearch import search
		except ImportError: 
			print("No module named 'google' found")
	# to search
		query = term
		for j in search(query, tld="co.in", num=intLength, stop=intLength, pause=2):
			embed.add_field(name="Result", value=f"{j}")
		embed.set_image(url='https://cdn.mos.cms.futurecdn.net/4TBgjGyyxufaKfztZy87Bk-1200-80.jpg')
		await ctx.send(embed=embed)

	@commands.command(name='egg')
	async def _egg(self, ctx):
		embed = discord.Embed(title="egg", description="egg")
		embed.add_field(name="egg", value="egg")
		embed.set_image(url='https://api.time.com/wp-content/uploads/2019/01/gettyimages-914246230.jpg')
		await ctx.send(embed=embed)
		
def setup(bot):
	bot.add_cog(Fun(bot))
