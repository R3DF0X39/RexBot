#! python3
#!/usr/bin/python
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands

class ping:#This is like the section of each command, when you see the help menu for the bot you will understand

    def __init__(self, bot):#This is the define so in this case its "self.bot", you can also add loop and extras to this
        self.bot = bot

    @commands.command(pass_context=True)#This is a command base
    async def ping(self, ctx):

        await self.bot.say("Pong")#This is code for a command

def setup(bot):
    n = ping(bot)
    bot.add_cog(n)#This is bot setup, every new command file you make must have this
