import discord
import asyncio
import array
import config.py
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = '-')

status = True

@bot.event
async def on_ready():
    print('Whitelist Bot by Mashhhyyy')
    print('Ready to run!')


@bot.command(pass_context = True)
async def toggle(ctx):
    if status == True:
        status = False
        await bot.say(':white_check_mark: Whitelist Toggled Off')
    elif status == False:
        status = True
        await bot.say(':white_check_mark: Whitelist Toggled On')


@bot.event
async def on_member_join(member):
    user = str(member)
    if str(member) not in config.whitelistedUsers:
        await bot.kick(str(member))
        if config.notifyOnKick == True:
            bot.send_message(config.notifyID, config.notifyMessage)


bot.run(config.TOKEN)