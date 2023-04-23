import os
from dotenv import load_dotenv
from twitchio.ext import commands
import time
from game import main
from threading import Thread
import queue



load_dotenv()
token = os.getenv("ACCESS_TOKEN")
client_id = os.getenv("CLIENT_ID")
channel_id = 633244077
headers = {
    "Authorization": f"Bearer {token}",
    "Client-Id": client_id,
    "Content-Type": "application/json",
}

class Bot(commands.Bot):
    def __init__(self, q):
        super().__init__(token=token, prefix="!", initial_channels=["mehmasha"])
        self.game_active = False
        self.players = {}
        self.q = q

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return
        print(message.author, message.author.id, message.content)
        me = await message.channel.user()

        await self.handle_commands(message)

    @commands.command(name="ping")
    async def pins(self, ctx):
        author = ctx.author.name
        await ctx.send(f"@{author}, pong!")

    @commands.command(name="move")
    async def pins(self, ctx, start, finish):
        author = ctx.author.name
        self.q.put_nowait(f'{start} {finish}')
        await ctx.send(f"@{author} ходит {start} {finish}!")




start_time = time.time()
q = queue.Queue()
bot = Bot(q)


try:
    # create two new threads
    t1 = Thread(target=bot.run)
    t2 = Thread(target=main, args=(q, ))

    # start the threads
    t1.start()
    t2.start()
    # start the threads
    t1.join()
    t2.join()
    # bot.run()
    # main()
finally:
    bot.loop.close()
