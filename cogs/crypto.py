import asyncio
import discord
import random
import re
from bs4 import BeautifulSoup
from datetime import datetime, date
from discord.ext import commands
import certifi
from pip._vendor import urllib3
import json

ERROR_READ = 'Error. Could not read data.'

def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

def get_content(filename):
    with open(filename) as file:
        content = [line.strip(' ') for line in file.readlines() if not line.strip(' ') == '']
    file.close()
    return content


def get_eur():
    global ERROR_READ
    url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD'
    page = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()).request('GET', url)
    soup = BeautifulSoup(page.data, 'html.parser')
    try:
        eur_price = soup.find('span', attrs={'class': 'uccResultAmount'}).text
        eur_price = '€' + eur_price
        print(eur_price)
        return "EUR: {}".format(eur_price)
    except AttributeError:
        return ERROR_READ


def get_bitcoin():
    global ERROR_READ
    url = 'https://www.worldcoinindex.com/coin/bitcoin'
    page = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()).request('GET', url)
    soup = BeautifulSoup(page.data, 'html.parser')
    try:
        bitcoin_price = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coinprice'}).text
        bitcoin_price = re.sub("[^0-9.,$]", "", bitcoin_price)
        print(bitcoin_price)
        bitcoin_change = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coin-percentage'}).text
        bitcoin_change = re.sub("[^0-9.,%\-+]", "", bitcoin_change)
        print(bitcoin_change)
        return "BTC: {}, change: {}".format(bitcoin_price, bitcoin_change)
    except AttributeError:
        return ERROR_READ

def get_usdt():
    global ERROR_READ
    url = 'https://www.worldcoinindex.com/coin/tether'
    page = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()).request('GET', url)
    soup = BeautifulSoup(page.data, 'html.parser')
    try:
        usdt_price = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coinprice'}).text
        usdt_price = re.sub("[^0-9.,$]", "", usdt_price)
        print(usdt_price)
        usdt_change = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coin-percentage'}).text
        usdt_change = re.sub("[^0-9.,%\-+]", "", usdt_change)
        print(usdt_change)
        return "USDT: {}, change: {}".format(usdt_price, usdt_change)
    except AttributeError:
        return ERROR_READ
    
def get_bch():
    global ERROR_READ
    url = 'https://www.worldcoinindex.com/coin/bitcoincash'
    page = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()).request('GET', url)
    soup = BeautifulSoup(page.data, 'html.parser')
    try:
        bch_price = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coinprice'}).text
        bch_price = re.sub("[^0-9.,$]", "", bch_price)
        print(bch_price)
        bch_change = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coin-percentage'}).text
        bch_change = re.sub("[^0-9.,%\-+]", "", bch_change)
        print(bch_change)
        return "BCH: {}, change: {}".format(bch_price, bch_change)
    except AttributeError:
        return ERROR_READ    
    

def get_ethereum():
    global ERROR_READ
    url = 'https://www.worldcoinindex.com/coin/ethereum'
    page = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()).request('GET', url)
    soup = BeautifulSoup(page.data, 'html.parser')
    try:
        eth_price = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coinprice'}).text
        eth_price = re.sub("[^0-9.,$]", "", eth_price)
        print(eth_price)
        eth_change = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coin-percentage'}).text
        eth_change = re.sub("[^0-9.,%\-+]", "", eth_change)
        print(eth_change)
        return "ETH: {}, change: {}".format(eth_price, eth_change)
    except AttributeError:
        return ERROR_READ

def get_cspn():
    global ERROR_READ
    url = 'https://www.worldcoinindex.com/coin/cryptosports'
    page = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()).request('GET', url)
    soup = BeautifulSoup(page.data, 'html.parser')
    try:
        cspn_price = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coinprice'}).text
        cspn_price = re.sub("[^0-9.,$]", "", cspn_price)
        print(cspn_price)
        cspn_change = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coin-percentage'}).text
        cspn_change = re.sub("[^0-9.,%\-+]", "", cspn_change)
        print(cspn_change)
        return "CSPN: {}, change: {}".format(cspn_price, cspn_change)
    except AttributeError:
        return ERROR_READ


currencies = {
    'btc': get_bitcoin,
    'eur': get_eur,
    'eth': get_ethereum,
    'usdt': get_usdt,
    'bch': get_bch,
    'cspn': get_cspn
}


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
Bot = discord.client
client = bot
client.remove_command('help')

class Crypto(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

        # Events

    @commands.Cog.listener()
    async def on_ready(self):
        print('Crypto Loaded')

    @commands.command(aliases=['Bitcoin'])
    async def btc(self, ctx, currency='btc', interval: int = 2, hour=datetime.now().hour, input_date=str(date.today())):
        global ERROR_READ
        global currencies
        interval *= 60
        input_date = [int(item) for item in input_date.split('-')]
        try:
            print("Processing currency price")
            input_date = date(*input_date)
            print("Done processing currency")
        except ValueError:
            print('Invalid time format.')
        hour = int(hour)

        while date.today() <= input_date and datetime.now().hour <= hour:
            try:
                data = currencies[currency]()
                if not data == ERROR_READ:
                    value = random.randint(0, 0xffffff)
                    embed = discord.Embed( colour=value)

                    embed.set_author(name="💰Bitcoin 💰", icon_url="https://cdn.discordapp.com/attachments/575735287146348545/733352430422720652/Untitled-1.png")

                    embed.add_field(name=f"{data}", value="\u200b", inline=False)

                    await ctx.send(embed=embed)
                    return
                else:
                    await ctx.send(f'{ERROR_READ}')
                    break
            except KeyError:
                await ctx.send('Invalid currency.')
                break

    @commands.command(aliases=['ethereum'])
    async def eth(self, ctx, currency='eth', interval: int = 2, hour=datetime.now().hour, input_date=str(date.today())):
        global ERROR_READ
        global currencies
        interval *= 60
        input_date = [int(item) for item in input_date.split('-')]
        try:
            print("Processing currency price")
            input_date = date(*input_date)
            print("Done processing currency")
        except ValueError:
            print('Invalid time format.')
        hour = int(hour)

        while date.today() <= input_date and datetime.now().hour <= hour:
            try:
                data = currencies[currency]()
                if not data == ERROR_READ:
                    value = random.randint(0, 0xffffff)
                    embed = discord.Embed( colour=value)
                    embed.set_author(name="💰 Ethereum 💰", icon_url="https://cdn.discordapp.com/attachments/575735287146348545/733359526660669484/Untitled-1.png")
                    embed.add_field(name=f"{data}", value="\u200b", inline=False)

                    await ctx.send(embed=embed)
                    return
                else:
                    await ctx.send(f'{ERROR_READ}')
                    break
            except KeyError:
                await ctx.send('Invalid currency.')
                break
                

    @commands.command(aliases=['tether'])
    async def usdt(self, ctx, currency='usdt', interval: int = 2, hour=datetime.now().hour, input_date=str(date.today())):
        global ERROR_READ
        global currencies
        interval *= 60
        input_date = [int(item) for item in input_date.split('-')]
        try:
            print("Processing currency price")
            input_date = date(*input_date)
            print("Done processing currency")
        except ValueError:
            print('Invalid time format.')
        hour = int(hour)

        while date.today() <= input_date and datetime.now().hour <= hour:
            try:
                data = currencies[currency]()
                if not data == ERROR_READ:
                    value = random.randint(0, 0xffffff)
                    embed = discord.Embed( colour=value)
                    embed.set_author(name="💰 Tether 💰", icon_url="https://cdn.discordapp.com/attachments/575735287146348545/733359119360327740/Untitled-1.png")

                    embed.add_field(name=f"{data}", value="\u200b", inline=False)

                    await ctx.send(embed=embed)
                    return
                else:
                    await ctx.send(f'{ERROR_READ}')
                    break
            except KeyError:
                await ctx.send('Invalid currency.')
                break


                
    @commands.command(aliases=['BitcoinCash'])
    async def bch(self, ctx, currency='bch', interval: int = 2, hour=datetime.now().hour, input_date=str(date.today())):
        global ERROR_READ
        global currencies
        interval *= 60
        input_date = [int(item) for item in input_date.split('-')]
        try:
            print("Processing currency price")
            input_date = date(*input_date)
            print("Done processing currency")
        except ValueError:
            print('Invalid time format.')
        hour = int(hour)

        while date.today() <= input_date and datetime.now().hour <= hour:
            try:
                data = currencies[currency]()
                if not data == ERROR_READ:
                    value = random.randint(0, 0xffffff)
                    embed = discord.Embed( colour=value)
                    embed.set_author(name="💰 Bitcoin Cash 💰", icon_url="https://cdn.discordapp.com/attachments/575735287146348545/733354743061020702/Untitled-1.png")

                    embed.add_field(name=f"{data}", value="\u200b", inline=False)

                    await ctx.send(embed=embed)
                    return
                else:
                    await ctx.send(f'{ERROR_READ}')
                    break
            except KeyError:
                await ctx.send('Invalid currency.')
                break

    @commands.command(aliases=['cryptosports'])
    async def cspn(self, ctx, currency='cspn', interval: int = 2, hour=datetime.now().hour, input_date=str(date.today())):
        global ERROR_READ
        global currencies
        interval *= 60
        input_date = [int(item) for item in input_date.split('-')]
        try:
            print("Processing currency price")
            input_date = date(*input_date)
            print("Done processing currency")
        except ValueError:
            print('Invalid time format.')
        hour = int(hour)

        while date.today() <= input_date and datetime.now().hour <= hour:
            try:
                data = currencies[currency]()
                if not data == ERROR_READ:
                    value = random.randint(0, 0xffffff)
                    embed = discord.Embed(colour=value)

                    embed.set_author(name="💰 Crypto Sports 💰", icon_url="https://assets.coingecko.com/coins/images/7826/large/cspn_logo_250.png?1551057201")
                    embed.add_field(name=f"{data}", value="\u200b", inline=False)

                    await ctx.send(embed=embed)
                    return
                else:
                    await ctx.send(f'{ERROR_READ}')
                    break
            except KeyError:
                await ctx.send('Invalid currency.')
                break



def setup(bot):
    bot.add_cog(Crypto(bot))
    print('Crypto Loaded')
