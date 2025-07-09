import os
from twitchio.ext import commands

# As informações são puxadas do Railway (Environment Variables)
TWITCH_TOKEN = os.environ['TWITCH_TOKEN']
BOT_USERNAME = os.environ['BOT_USERNAME']
TWITCH_CHANNEL = os.environ['TWITCH_CHANNEL']

class Bot(commands.Bot):

    def __init__(self):
        # Inicializa o bot com as credenciais
        super().__init__(
            token=TWITCH_TOKEN,
            prefix='!',
            initial_channels=[TWITCH_CHANNEL]
        )

    async def event_ready(self):
        # Mensagem que aparece no log do Railway quando o bot conecta
        print(f'Bot {self.nick} logado e pronto!')
        print(f'Conectado no canal: {TWITCH_CHANNEL}')

    # --- SEUS COMANDOS PERSONALIZADOS COMEÇAM AQUI ---

    @commands.command(name='salve')
    async def cmd_salve(self, ctx: commands.Context):
        # Manda um salve para quem digitou o comando
        await ctx.send(f'Um salve especial para você, {ctx.author.name}! Tamo junto na live!')

    @commands.command(name='discord')
    async def cmd_discord(self, ctx: commands.Context):
        # Coloque o seu link do Discord aqui
        await ctx.send('Quer fazer parte da família? Cola no nosso Discord: [https://discord.gg/AjXDDJdFub]')

    @commands.command(name='instagram')
    async def cmd_instagram(self, ctx: commands.Context):
        # Coloque o link do seu Instagram aqui
        await ctx.send('Para não perder nada, segue lá no Insta: [https://www.instagram.com/snow_pr25?igsh=MTNsNnA2d2xlMG9jdA==]')

    @commands.command(name='altura')
    async def cmd_altura(self, ctx: commands.Context):
        # Coloque o IP do seu servidor SAMP aqui
        await ctx.send('Nosso servidor no SAMP é: [179.127.16.157:29015]')
        
    # Adicione mais comandos aqui se precisar

# Ponto de partida para rodar o bot
if __name__ == "__main__":
    bot = Bot()
    bot.run()
