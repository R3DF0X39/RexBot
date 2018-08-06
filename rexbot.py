import discord
from discord.ext import commands
import sys, traceback
from os import listdir
from os.path import isfile, join



def get_prefix(bot, message):

    prefixes = ['$']

    return commands.when_mentioned_or(*prefixes)(bot, message)

cmd_dir = "commands"

bot = commands.Bot(command_prefix=get_prefix, description='R3dfox')

if __name__ == "__main__":
    for extension in [f.replace('.py', '') for f in listdir(cmd_dir) if isfile(join(cmd_dir, f))]:
        try:
            bot.load_extension(cmd_dir + "." + extension)
        except Exception as e:
            print(f'Failed to load file {extension}.')
            traceback.print_exc()

@bot.event
async def on_ready():

    print("Starting up")
    print(f'Started!')


bot.run('paste token here', bot=True, reconnect=True)
