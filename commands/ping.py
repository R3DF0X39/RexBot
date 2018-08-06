#! python3
#!/usr/bin/python
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import datetime
import time
from random import choice, randint

class ping:#This is like the section of each command, when you see the help menu for the bot you will understand

    def __init__(self, bot):#This is the define so in this case its "self.bot", you can also add loop and extras to this
        self.bot = bot

    @commands.command(pass_context=True)#This is a command base
    async def ping(self, ctx):
        t1 = time.perf_counter()
        await self.bot.send_typing(ctx.message.channel)
        t2 = time.perf_counter() 
        ping = str(round((t2-t1)*1000)) 
        author = ctx.message.author.mention
        response = await self.bot.say("**{}, this took me {}ms to send**".format(author, ping))
        issue = ctx.message
        time.sleep(10)
        await self.bot.delete_message(response)
        time.sleep(0.5)
        await self.bot.delete_message(issue)
        
        

def setup(bot):
    n = ping(bot)
    bot.add_cog(n)#This is bot setup, every new command file you make must have this
