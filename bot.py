import discord
from discord.ext import commands
from async_rickroll_detector import RickRollDetector

BOT_TOKEN = "put your god dammn bot token here"
RICKROLL_FOUND_MESSAGE = "Định rickroll ak =)) k dễ đâu con :trollface:" #rickroll detect messages 

bot = commands.Bot(command_prefix = ">", intents = discord.Intents.default())

@bot.event
async def on_ready():
    global detector
    detector = RickRollDetector()

@bot.event
async def on_message(msg):
    for i in msg.content.split(" "):
        i = i.replace("<","").replace(">", "") #Removes <> that could be used to hide embeds
        if "https://" in i and await detector.find(i):
            await msg.reply(RICKROLL_FOUND_MESSAGE)
            break

    await bot.process_commands(msg)

bot.run(BOT_TOKEN) #u already put ur token above
