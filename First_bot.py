import discord
from discord.ext import commands
from discord.ui import View
intents = discord.Intents().all()

bot=commands.Bot(command_prefix="°",description="Bot de Flavie", intents=intents)

@bot.event
async def on_ready():
    print("Ready!")

@bot.command()
async def coucou(ctx):
    await ctx.send("Coucou !") #appel reseau

@bot.command()
async def serverInfo(ctx):
    server=ctx.guild
    numberOfTextChannels=len(server.text_channels)
    numberOfVoiceChannels=len(server.voice_channels)
    serverDescription=server.description
    numberOfPerson=server.member_count
    serverName=server.name
    global message
    message=f"Le serveur{serverName} contient {numberOfPerson} personnes. \n La description du server est: {serverDescription}. \n Ce serveur possède {numberOfTextChannels} salons écrits ainsi que {numberOfVoiceChannels} salons vocaux."
    
    await ctx.send(message)

@bot.command()
async def say(ctx,*texte):
    await ctx.send(" ".join(texte))

@bot.command()
async def repeat(ctx):
    lastMessage=message;
    await ctx.send(lastMessage)



@bot.command()
async def favoriteMusic(ctx):
    music="Quelle est ta musique préférée?"
    await ctx.send(music)

@bot.command()
async def thisMusicIs(ctx,*texte):
    await ctx.send("C'est "+" ".join(texte))

# @bot.event
# async def button(interaction):
#     if interaction.component.label.startswith("Default Button"):
#         await interaction.respond(type=InteractionType.ChannelMessageWithSource, content='Button Clicked')

@bot.command() # Create a command inside a cog
async def button(ctx):
    
    view = discord.ui.View() # Establish an instance of the discord.ui.View class
    style = discord.ButtonStyle.red  # The button will be gray in color
    item = discord.ui.Button(style=style, label="Riptide", url="https://www.youtube.com/watch?v=lYoWuaw5nSk")  # Create an item to pass into the view class.
    view.add_item(item=item)  # Add that item into the view class
    await ctx.send("This message has buttons!", view=view)  # Send your message with a button.
#on demarre le bot
bot.run("MTAyMjUyNzg0ODAwODkyNTIzNg.GB_6Z1.aOCmJOIGmothq8MG7j1JnOpOmjiCxeELJl2jiI")
