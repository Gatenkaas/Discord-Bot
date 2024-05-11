import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

# Functie om te controleren of de auteur van het bericht de eigenaar is
def is_owner(ctx):
    return ctx.message.author.id == '657941147347451905' # Vervang 'your_discord_user_id_here' door jouw Discord gebruikers-ID

# Commando om de bot uit te schakelen
@client.command()
@commands.check(is_owner)
async def shutdown(ctx):
    await ctx.send("Bot wordt uitgeschakeld...")
    await client.close()

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')

@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def Eigenaar(ctx, member: discord.Member):
    await ctx.send(f"De eigenaar(en) zijn stijnieboy_150 en bobveeman {member.mention}!")

@client.command()
async def echo(ctx, *, message):
    await ctx.send(message)

@client.command()
async def ip(ctx):
    await ctx.send("Server is nog in productie")

@client.command()
async def wakker(ctx):
    await ctx.send("Ja ben nog wakker {member.mention}")

@client.command()
async def github(ctx):
    await ctx.send("github.com/Gatenkaas")

@client.command()
async def website(ctx):
    await ctx.send("gatenkaas.github.io/Website")


client.run('Bot_token_here')