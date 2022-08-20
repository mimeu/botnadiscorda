import discord
TOKEN = 'MTAxMDIzMzk5NjEyODU2NzQ1OA.GHqOH-.sNK-vf7OvTmM0aotSFhjR4Ab_v5FEb25gnGwX0'
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(':kdd:')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'u':
        await message.channel.send("u")


client.run(TOKEN)
