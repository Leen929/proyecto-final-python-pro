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
        "el anime trata sobre un grupo de personas que tienen inmortalidad": 
        { "nombre": "Los 7 pecados capitales", "imagen": "imagenes/seven.jpg" },
        "una batalla entre dioses y humanos": 
        { "nombre": "el anime se llama record of ragnarok", "imagen": "imagenes/record.png" },
        "videojuego que trata sobre un grupo de personajes principales van en un tren espacial ": 
        {"nombre": "El videojuego se llama Honkai:Star Rail","imagen": "imagenes/honkai.png" },
        "videojuego sobre mundo abierto y exploras siete naciones elementales": 
        {"nombre": "El videojuego se llama Genshin Impact", "imagen": "imagenes/genshin.png" },
        "Anime sobre ninjas muy famoso": 
        { "nombre": "Naruto", "imagen": "imagenes/naruto.jpg" },
        "Anime sobre cazadores de demonios, la hermana de un niño se vuelve demonio": 
        { "nombre": "EL anime se llama Demon Slayer", "imagen": "imagenes/demon slaye.jpg" },
        "Anime sobre dos niños pasando un examen para cazadores y obtener su licencia": 
        { "nombre": "El anime se llama HUNTER X HUNTER", "imagen": "imagenes/hunter.avif" },
        "videojuego que trata sobre galletas de difentes sabores y hacer tu propio reino": 
        { "nombre": "El videojuego se llama Cookie Run:Kingdom", "imagen": "imagenes/cookie.webp" },
        "Anime de de heroes historicos como sirvientes en una guerra santa ": 
        { "nombre": "Fate Stay Night", "imagen": "imagenes/fate.jpg" },
        "Anime de piratas y el prota es de goma y se estira mucho, tiene demasiados capitulos":
        { "nombre": "ONE PIECE", "imagen": "imagenes/onepiece.jpeg" },
        "videojuego que trata de zombies intentando entrar a tu casa y plantas la defienden":
        { "nombre": "Plantas vs Zombies", "imagen": "imagenes/plantas.webp" },
        "Franqucia de videojuegos de ser guardia de noche en una pizzeria": 
        { "nombre": "Five Nights At freddy's", "imagen": "imagenes/FiveNightsAtFreddys.webp" },
        "Videojuego en donde un niño cae al mundo de los monstrous y conoce dos hermanos esqueleto": 
        { "nombre": "Undertale", "imagen": "imagenes/undertale.webp" },
        "Videojuego en donde eres un pequeño caballero de un reino muerto y bajas a las profundides":
        { "nombre": "Hollow Knight", "imagen": "imagenes/Hollow_Knight.jpg" },
        "Anime en donde una elfa era parte de un grupo de héroes ahora casi muertos y hace un nuevo viaje": 
        { "nombre": "Frieren Beyond Journey's end" , "imagen": "imagenes/frieren.jpg" },
        "Anime de una apotecaria de la antigua china que trabaja en el palacio real y le encantan los venenos": 
        { "nombre": "the apothecary's diary", "imagen": "imagenes/maomao.jpg" },
        "Videojuego de un humano mitad demonio que es mercenario y tiene una empresa caza demonios": 
        { "nombre": "Devil May Cry", "imagen": "imagenes/devil.jpg" },
        "Videojuego de un prota que se llama Leon S. Kennedy y es policia de casos sobrenaturales o armas biológicas": 
        { "nombre": "Resident Evil 4", "imagen": "imagenes/resident.jpg" },
        "Videojuego donde personas viven cosas sobrenaturales a partir de su decayente salud mental o sus situaciones": 
        { "nombre": "Silent Hill", "imagen": "imagenes/silent hill.avif" },
        "Anime de detectives contra una mafia, los personajes tiene abilidades sobrenaturales y estan basados en autores reales": 
        { "nombre": "Bungo Stray Dogs", "imagen": "imagenes/bungo.jpg" },
        "Un videojuego de una infección fungica, la prota es inmune al hongo": 
        { "nombre": "The Last Of Us", "imagen": "imagenes/last of us.jpg" }
    }
    anime_lower = anime.lower().strip()
    for letra, respuesta in lista_animes.items():
        if anime_lower in letra.lower():
            await ctx.send(respuesta["nombre"])
            archivo = discord.File(respuesta["imagen"])
            await ctx.send(file=archivo)
            return
    await ctx.send("❌ No reconozco ese anime o videojuego, ¡intenta con otro fragmento!")

bot.run("")

