#! python3
#!/usr/bin/python
# -*- coding: utf-8 -*-
import discord
import urllib.request
import urllib.error
import urllib.parse
import json
from discord.ext import commands
import time

class test:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def test(self , ctx, language, *, input : str):#This is like the command input, so for this one you have to say "say (input)" and it will output the input
        """Usage: $test <language #> <code> language #s, visit rextester.com/main"""
        try:
            #embed creation
            await self.bot.send_typing(ctx.message.channel)
            author = ctx.message.author
            create=discord.Embed(description="Loading", colour=discord.Colour(value=0xff7373))
            create.set_author(name="Rex Tester", icon_url="https://i.imgur.com/n9q9nBU.png")
            create.set_footer(text="Command issued by {}".format(author))
            start = await self.bot.say(embed=create)
            time.sleep(1)
            url = 'http://rextester.com/rundotnet/api'
            postdata = urllib.parse.urlencode({
                'LanguageChoice': language,
                'Program': input,
                'Input': "",
                'CompilerArgs': "",
                })
            postdatabytes = str.encode(postdata)
            req = urllib.request.Request(url, postdatabytes)
            response = urllib.request.urlopen(req)
            output = response.read()
            #print 'API response: ' + output
            response_decoded = json.loads(output)
            warns = response_decoded["Warnings"]
            er = response_decoded["Errors"]
            re = response_decoded["Result"]
            st = response_decoded["Stats"]
            #print "Decoded JSON:"
            #print response_decoded
            author2 = ctx.message.author.mention
            
            build5=discord.Embed(colour=discord.Colour(value=0xffb200))
            build5.set_author(name="Rex Tester", icon_url="https://i.imgur.com/n9q9nBU.png")
            build5.add_field(name="Warnings", value="Not started", inline=False)
            build5.add_field(name="Errors", value="Not started", inline=False)
            build5.add_field(name="Stats", value="Not started", inline=False)
            build5.add_field(name="Result", value="Not started", inline=False)
            build5.set_footer(text="Command issued by {}".format(author))
            buildprint5 = await self.bot.edit_message(start, embed=build5)
            await self.bot.send_typing(ctx.message.channel)

            #Adding results
            time.sleep(0.5)
            add=discord.Embed(colour=discord.Colour(value=0xffb200))
            add.set_author(name="Rex Tester", icon_url="https://i.imgur.com/n9q9nBU.png")
            add.add_field(name="Warnings", value="```{}```".format(warns), inline=False)
            add.add_field(name="Errors", value="Not started", inline=False)
            add.add_field(name="Stats", value="Not started", inline=False)
            add.add_field(name="Result", value="Not started", inline=False)
            add.set_footer(text="Command issued by {}".format(author))
            addprint = await self.bot.edit_message(buildprint5, embed=add)
            await self.bot.send_typing(ctx.message.channel)
            time.sleep(0.5)
            add2=discord.Embed(colour=discord.Colour(value=0xffb200))
            add2.set_author(name="Rex Tester", icon_url="https://i.imgur.com/n9q9nBU.png")
            add2.add_field(name="Warnings", value="```{}```".format(warns), inline=False)
            add2.add_field(name="Errors", value="```{}```".format(er), inline=False)
            add2.add_field(name="Stats", value="Not started", inline=False)
            add2.add_field(name="Result", value="Not started", inline=False)
            add2.set_footer(text="Command issued by {}".format(author))
            addprint2 = await self.bot.edit_message(addprint, embed=add2)
            await self.bot.send_typing(ctx.message.channel)
            time.sleep(0.5)
            add3=discord.Embed(colour=discord.Colour(value=0xffb200))
            add3.set_author(name="Rex Tester", icon_url="https://i.imgur.com/n9q9nBU.png")
            add3.add_field(name="Warnings", value="```{}```".format(warns), inline=False)
            add3.add_field(name="Errors", value="```{}```".format(er), inline=False)
            add3.add_field(name="Stats", value="```{}```".format(st), inline=False)
            add3.add_field(name="Result", value="Not started", inline=False)
            add3.set_footer(text="Command issued by {}".format(author))
            addprint3 = await self.bot.edit_message(addprint2, embed=add3)
            await self.bot.send_typing(ctx.message.channel)
            time.sleep(0.5)
            add4=discord.Embed(colour=discord.Colour(value=0xffb200))
            add4.set_author(name="Rex Tester", icon_url="https://i.imgur.com/n9q9nBU.png")
            add4.add_field(name="Warnings", value="```{}```".format(warns), inline=False)
            add4.add_field(name="Errors", value="```{}```".format(er), inline=False)
            add4.add_field(name="Stats", value="```{}```".format(st), inline=False)
            add4.add_field(name="Result", value="```{}```".format(re), inline=False)
            add4.set_footer(text="Command issued by {}".format(author))
            addprint4 = await self.bot.edit_message(addprint3, embed=add4)
            await self.bot.send_typing(ctx.message.channel)
            time.sleep(0.3)
            add5=discord.Embed(colour=discord.Colour(value=0x35bf4d))
            add5.set_author(name="Rex Tester", icon_url="https://i.imgur.com/n9q9nBU.png")
            add5.add_field(name="Warnings", value="```{}```".format(warns), inline=False)
            add5.add_field(name="Errors", value="```{}```".format(er), inline=False)
            add5.add_field(name="Stats", value="```{}```".format(st), inline=False)
            add5.add_field(name="Result", value="```{}```".format(re), inline=False)
            add5.set_footer(text="Command issued by {}".format(author))
            addprint5 = await self.bot.edit_message(addprint4, embed=add5)
            await self.bot.say("**{}, Done :thumbsup:**".format(author2))
            await self.bot.send_typing(ctx.message.channel)

        except Exception as e:
            await self.bot.say("I have ran into a error :x:")
            raise
    #It is a dict called response. I have to call specific keys from within the dict
    #I would think just replace the "print" with the bot.say

def setup(bot):
    n = test(bot)
    bot.add_cog(n)
