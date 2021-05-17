import discord
from discord.ext import commands
import asyncio

#create Moderation cog
class Moderation(commands.Cog):
	def __init__(self, bot):
		self.bot=bot
	
	#ban command
	@commands.command(name="ban")
	@commands.has_permissions(ban_members=True)
	async def _ban(self, ctx, member: discord.Member, *, reason=None):
		if reason == None:
			reason = "being rude"
		await ctx.send(f"{member.mention} has been banned by {ctx.message.author.mention} for {reason}")
		await member.ban(reason=reason)
		await member.send(f"You have been banned in {ctx.guild} for {reason}")
		
	#kick command
	@commands.command(name="kick")
	@commands.has_permissions(kick_members=True)
	async def _kick(self, ctx, member: discord.Member, *, reason=None):
		if reason == None:
			reason = "being rude"
		await ctx.send(f"{member.mention} has been banned by {ctx.message.author.mention} for {reason}")
		await member.kick(reason=reason)
		await member.send(f"You have been banned in {ctx.guild} for {reason}")

	#mute command
	@commands.command(name="mute")
	@commands.has_permissions(manage_messages=True)
	async def _mute(self, ctx, member: discord.Member, duration=None, *, reason=None):
		if reason == None:
			reason = "being rude"
		mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
		if duration == None:
			if not mutedRole:
				mutedRole = await ctx.guild.create_role(name="Muted")
				for channel in ctx.guild.channels:
					channel.set_permissions(mutedRole, read_messages=False, send_messages=False, read_message_history=False, speak=False)
			else:
				await ctx.send("Member is already muted")
			await member.add_role(mutedRole)
			await ctx.send(f"{member.mention} has been muted by {ctx.message.author.mention} for {reason}")
			await member.send(f"You have been muted in {ctx.guild} for {reason}")
			pass
		if not mutedRole:
			mutedRole = await ctx.guild.create_role(name="Muted")
			for channel in ctx.guild.channels:
				channel.set_permissions(mutedRole, read_messages=False, send_messages=False, read_message_history=False, speak=False)
		else:
			await ctx.send("User is already muted")
		await member.add_role(mutedRole)
		await ctx.send(f"{member.mention} has been muted by {ctx.message.author.mention} for {reason}")
		await member.send(f"You have been muted in {ctx.guild} for {reason}")
		newTime = int(duration)
		finalTime = newTime*60
		await asyncio.sleep(finalTime)
		await member.remove_role(mutedRole)
		await member.send(f"You are now unmuted in {ctx.guild}")
		
		@commands.command(name="unmute")
		@commands.has_permissions(manage_messages=True)
		async def _unmute(self, ctx, member: discord.Member):
			mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
			if not mutedRole:
				await ctx.send("Member is not muted")
			else:
				await member.remove_role(mutedRole)
		
		@commands.command(name="unban")
		@commands.has_permissions(ban_members=True)
		async def _unban(self, ctx, member: discord.Member):
			bannedUsers = ctx.guild.bans()
			member_name, member_discriminator = member.split('#')
			for banEntry in bannedUsers:
				user=banEntry.user
				if (user.name, user.discriminator) == (member_name, member_discriminator):
					await ctx.guild.unban(user)
					await ctx.send(f"User has been unbanned")
					return

		@commands.command(name="softban")
		@commands.has_permissions(ban_members=True)
		async def _softban(self, ctx, member: discord.Member, duration, *, reason=None):
			if reason == None:
				reason = "being rude"
			await ctx.send(f"{member.mention} is now banished from {ctx.guild} by {ctx.message.author.mention} for {reason}. They may return after {duration} minutes")
			await member.send(f"You have been banned from {ctx.guild} for {reason}. You may return after {duration} minutes.")
			await member.ban(reason=reason)
			newTime = int(duration)
			finalTime = newTime*60
			await asyncio.sleep(finalTime)
			await ctx.guild.unban(member)
			await member.send(f"You are now allows back into {ctx.guild}")
				
	@commands.command(name="hackban")
	@commands.has_permissions(ban_members=True)
	async def _hackban(self, ctx, member: discord.Member, *, reason=None):
		if reason == None:
			reason = "being rude"
		await ctx.send(f"{member.mention} has been hackbanned from {ctx.guild} by {ctx.message.author.mention} for {reason}")
		await member.send(f"You have been hackbanned from {ctx.guild} for {reason}")
		await member.ban(reason=reason)
		await asyncio.sleep(3)
		await ctx.guild.unban(member)

	@commands.command(name='userinfo')
	async def _userinfo(self, ctx, *, member: discord.Member=None):
		if member == None:
			member = ctx.message.author
		roles = [role for role in member.roles if role != ctx.guild.default_role]
		embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
		embed.set_author(name=f"User Info - {member}")
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer (text=f"Requested by {ctx.author}")
		embed.add_field(name="ID", value=member.id)
		embed.add_field(name="Display Name", value=member.display_name)
		embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I %M %p UTC"))
		embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I %M %p UTC"))
		embed.add_field(name=f"(Roles, {len(roles)}", value=" ".join([role.mention for role in roles]))
		embed.add_field(name="Top Role:", value=member.top_role.mention)
		embed.add_field(name="Bot?", value=member.bot)
		await ctx.send(embed=embed)

		
	@commands.command(name='avatar')
	async def _avatar(self, ctx, *, member: discord.Member=None):
		if member == None:
			member = ctx.message.author
		embed=discord.Embed(title=f"{member.name}'s Avatar", color=member.color, timestamp=ctx.message.created_at)
		embed.set_thumbnail(url=member.avatar_url)
		await ctx.send(embed=embed)

	@commands.command(name='purge')
	@commands.has_permissions(manage_messages=True)
	async def _purge(self, ctx, amount):
		await ctx.message.delete()
		await ctx.send("Now purging...", delete_after=3)
		await asyncio.sleep(1)
		await ctx.channel.purge(amount=amount)
    
def setup(bot):
	bot.add_cog(Moderation(bot))
