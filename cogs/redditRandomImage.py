import discord
from discord.ext import commands
import json
import random

# Import short commands from json file
with open('./json/subreddits.json') as config:
    subreddit_list = json.load(config)


class RedditRandomImage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = self.bot.reddit
        self.subreddits_list = subreddit_list

    @commands.command()
    async def random(self, ctx, subreddit_name: str):
        try:
            img_request = self.reddit.subreddit(subreddit_name).random().url
            value = random.randint(0, 0xffffff)
            response = discord.Embed(color=value)
            response.set_image(url=img_request)

            await ctx.send(embed=response)
        except Exception as e:
            print("Got ({}) error from  {}".format(e, ctx.invoked_with))
            await ctx.send("I could not find `{}`".format(subreddit_name))

    @commands.command()
    async def meme(self, ctx):
        meme = self.reddit.subreddit("memes").random().url
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(
            colour=value,
        )

        embed.set_author(name="M E M E")
        embed.set_image(url=meme)
        embed.set_footer(text=f"{ctx.author} Just got memed", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(RedditRandomImage(bot))
