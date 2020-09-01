import discord
from discord.ext import commands
import json
import random
import datetime

def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix,  case_insensitive=True, owner_id=382947478422421516)
Bot = discord.client
client = bot
client.remove_command('help')
value = random.randint(0, 0xffffff)

class Moderation(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot


        #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation Cog is on')

        #Commands

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        channel = discord.utils.get(member.guild.channels, name='➤🍐resorter-logs')
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')
        embed2 = discord.Embed(
            colour=value,
        )
        embed2.set_author(name=f" {member}", icon_url=member.avatar_url)
        embed2.add_field(name=f'{member} was Banned for: {reason}', value=":cold_face::cold_face::cold_face::cold_face::cold_face::cold_face:", inline=False)
        await channel.send(embed=embed2) 

        print(f'{member} was Banned from a server')
        await member.send(f'You have been banned for:{reason}')

        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member: discord.Member):
        channel = discord.utils.get(member.guild.channels, name='➤🍐resorter-logs')
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        channel = discord.utils.get(member.guild.channels, name='➤🍐resorter-logs')
        embed2 = discord.Embed(
            colour=value,
        )
        embed2.set_author(name=f" {member}", icon_url=member.avatar_url)
        embed2.add_field(name=f'{member} was Unbaned', value=":cold_face::cold_face::cold_face::cold_face::cold_face::cold_face:", inline=False)
        await channel.send(embed=embed2)
        
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                print(f'{member} was Unbanned from a server')
                return
        
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member = None):
        channel = discord.utils.get(member.guild.channels, name='➤🍐resorter-logs')
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not member:
            await ctx.send('Please specify a member')
            return
        await member.add_roles(role)
        await ctx.send('Muted')
        embed2 = discord.Embed(
            colour=value,
        )
        embed2.set_author(name=f" {member}", icon_url=member.avatar_url)
        embed2.add_field(name=f'{member} was Muted', value=":cold_face::cold_face::cold_face::cold_face::cold_face::cold_face:", inline=False)
        await channel.send(embed=embed2) 
        print(f'{member} was Muted from a server')
        await member.send('You have been Muted')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member = None):
        channel = discord.utils.get(member.guild.channels, name='➤🍐resorter-logs')
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not member:
            await ctx.send('Please specify a member')
            return
        await member.remove_roles(role)
        await ctx.send('Unmuted')
        
        embed2 = discord.Embed(
            colour=value,
        )
        embed2.set_author(name=f" {member}", icon_url=member.avatar_url)
        embed2.add_field(name=f'{member} was umuted', value=":cold_face::cold_face::cold_face::cold_face::cold_face::cold_face:", inline=False)
        await channel.send(embed=embed2)
        
        print(f'{member} was Unmuted from a server')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        channel = discord.utils.get(member.guild.channels, name='➤🍐resorter-logs')
        await member.kick(reason=reason)
        print(f'{member} was Kicked from a server')
        
        embed2 = discord.Embed(
            colour=value,
        )
        embed2.set_author(name=f" {member}", icon_url=member.avatar_url)
        embed2.add_field(name=f'{member} was Kicked for: {reason}', value=":cold_face::cold_face::cold_face::cold_face::cold_face::cold_face:", inline=False)

        await channel.send(embed=embed2)
        await member.send(f'You have been Kicked for:{reason}')

    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=6):
        await ctx.channel.purge(limit=amount+1)

    @commands.command(aliases=['purgeall', 'purge_all'])
    @commands.has_permissions(manage_messages=True)
    async def clearall(self, ctx, amount=9999999999999):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def warn(self, ctx, member: discord.Member, *, reason):
        channel = discord.utils.get(member.guild.channels, name='➤🍐resorter-logs')
        value = random.randint(0, 0xffffff)
        await ctx.message.delete()
        embed = discord.Embed(colour=value, timestamp=datetime.datetime.utcnow())
        embed.add_field(name=f'{member} was warned for: {reason}', value="\u200b", inline=False)

        await ctx.send(embed=embed)
        
        embed2 = discord.Embed(
            colour=value,
        )
        embed2.set_author(name=f" {member}", icon_url=member.avatar_url)
        embed2.add_field(name=f'{member} was warned for: {reason}', value=":cold_face::cold_face::cold_face::cold_face::cold_face::cold_face:", inline=False)

        await channel.send(embed=embed2)
        await member.send(f'You have been warned for:{reason}')
        
        
        
    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def role(self, ctx, role: discord.Role, user: discord.Member):
        await user.add_roles(role, member)
        await ctx.send(f"{member} received {role}.")
        
    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def unrole(self, ctx, role: discord.Role, user: discord.Member):
        await user.remove_roles(role)
        await ctx.send(f"{user} got {role} removed.")
        
        #errors

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please select a user to kick.')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please select a user to ban.')           


def setup(bot):
    bot.add_cog(Moderation(bot))
    print('Moderation Loaded')
