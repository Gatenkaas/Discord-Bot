import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Servers soon?"))

@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def echo(ctx, *, message):
    await ctx.send(message)

@client.command()
async def wakker(ctx):
    await ctx.send(f"Ja ben nog wakker {ctx.message.author.mention}", reference=ctx.message

@client.command()
async def github(ctx):
    await ctx.send("github.com/Gatenkaas")

@client.command()
async def website(ctx):
    await ctx.send("gatenkaas.github.io/Website")

@client.command()
async def ip(ctx):
    embed = discord.Embed(
        title = "Gatenkaas Servers IP",
        description = " Hallo leuk dat je wilt spelen maar we gaan DIT WEEKEND OPEN HOERA BEN JIJ ERBIJ NODIG VRIENDEN UIT EN DAN GAAN de servers crashen we kunnen niet wachten helaas nog geen lobby event enzo heb geen geld maar soms als ik kan is er survival en ondertussen werken we door en als de servers klaar zijn en gekd heb wordt de survival wereld overgedragen naar de officiele servers zijn wij je op onze server?",
        color = discord.Color.yellow()
    )

    embed.set_author(name="Gatenkaas Servers", icon_url="https://p19-pu-sign-ie.tiktokcdn-eu.com/obj/tos-ie-avt-0068-ie/2102fd536f5fd417457344b94293fe2d?lk3s=a5d48078&x-expires=1715781600&x-signature=8Oi0ge%2FN9%2FRNiFMfWOcieLKYShw%3D")
    embed.add_field(name="Java", value="gatenkaas.aternos.me", inline=False)
    embed.add_field(name="Bedrock", value="gatenkaas.aternos.me", inline=False)
    embed.add_field(name="Bedrock Poort", value="47732", inline=False)

    await ctx.send(embed=embed)

client.run('Bot_token_here')
