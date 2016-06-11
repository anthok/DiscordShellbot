import discord
import asyncio
import requests
import utilities as utils
from settings import Settings

class ShellcodeBot(discord.Client):
    def __init__(self,settings='settings.txt'):
        super().__init__()
        self.settings = Settings(settings)

    def run(self):
        return super().run(self.settings.email, self.settings.password)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self,message):
        # don't reply to self
        if message.author == self.user:
            return
        if message.content.startswith('!shell_exec'):
            msg = message.content.split(' ')
            if len(msg) <= 1:
                return

            msg = utils.run_command(msg[1:])
            await self.send_message(message.channel, msg.decode("utf-8"))

if __name__ == "__main__":
    client = ShellcodeBot()
    client.run()
