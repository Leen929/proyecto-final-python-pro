import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def animes(ctx, *, anime: str):
    lista_animes = {
        "el anime trata sobre un grupo de personas que tienen inmortalidad": "Los 7 pecados capitales",
        "una batalla entre dioses y humanos": "el anime se llama record of ragnarok",
        "videojuego que trata sobre un grupo de personajes principales van en un tren espacial ": "El videojuego se llama Honkai:Star Rail",
        "videojuego sobre mundo abierto y exploras siete naciones elementales": "El videojuego se llama Genshin Impact",
        "Anime sobre ninjas muy famoso": "Naruto",
        "Anime sobre cazadores de demonios, la hermana de un niño se vuelve demonio": "EL anime se llama Demon Slayer",
        "Anime sobre dos niños pasando un examen para cazadores y obtener su licencia": "El anime se llama HUNTER X HUNTER",
        "videojuego que trata sobre galletas de difentes sabores y hacer tu propio reino": "El videojuego se llama Cookie Run:Kingdom",
        "Anime de de heroes historicos como sirvientes en una guerra santa ": "Fate Stray Night",
        "Anime de piratas y el prota es de goma y se estira mucho, tiene demasiados capitulos": "ONE PIECE",
    }
    anime_lower = anime.lower().strip()
    for letra, respuesta in lista_animes.items():
        if anime_lower in letra.lower():
            await ctx.send(respuesta)
            return
    await ctx.send("❌ No reconozco ese anime, ¡intenta con otro fragmento!")

bot.run("")
