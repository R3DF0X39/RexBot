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
            #print "Decoded JSON:"
            #print response_decoded
            await self.bot.say("**Warnings returned**\n```{}```".format(response_decoded["Warnings"]))
            time.sleep(0.5)
            await self.bot.say("**Errors returned**\n```{}```".format(response_decoded["Errors"]))
            time.sleep(0.5)
            await self.bot.say("**Result**\n```{}```".format(response_decoded["Result"]))
            time.sleep(0.5)
            await self.bot.say("**Stats**\n```{}```".format(response_decoded["Stats"]))
        except Exception as e:
            await self.bot.say("I have ran into a error :x:")
            raise
    #It is a dict called response. I have to call specific keys from within the dict
    #I would think just replace the "print" with the bot.say

def setup(bot):
    n = test(bot)
    bot.add_cog(n)
