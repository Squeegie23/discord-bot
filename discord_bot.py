import discord

TOKEN = 'MTAwMzc3MzgwMzc0ODQwNTI5OQ.GGn4Sy.yMXr9E6jdU49NUBGD81khTiFtHYOhm2RKaHsSA'

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} is rdy to fuggin go'.format(client))

@client.event
async def on_message(text):
    username = str(text.author).split('#')[0]
    user_message = str(text.content)
    channel = str(text.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if text.author == client.user:
        return

    if text.channel.name == 'bot-spam':
        if user_message.lower() == 'hello':
            await text.channel.send(f'Hi, i did it! {username}')
            return

    if user_message.lower() == '!hello':
        await text.channel.send('I REALLY DONE DID THE THING')
        return

    if client.user.mentioned_in(text):
        await text.channel.send('ACTUALLY DID IT THIS TIME <:dab:390534211632627713>')
        return

client.run(TOKEN)