import discord
import random
import os
from discord.ext import commands


client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('with gifs'))
  print('Bot is ready')


@client.command()
async def ping(ctx):
  await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command()
async def add(ctx,arg1):
  f= open("member_list.txt",'r')
  x=f.read()
  members= x.split(',')
  if arg1 in members:
    await ctx.send("the member is already added")
  else:
    a= open("member_list.txt",'a')
    a.write(','+arg1)
    a.close()
  f.close()

devs=['<@!724635448781307954>','<@!889064920820371466>']

    

@client.command()
async def delete(ctx):
        await ctx.channel.delete()
        new_channel = await ctx.channel.clone(reason="Channel was purged")
        await new_channel.edit(position=ctx.channel.position)
        await new_channel.send("Channel was purged")

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')



client.run('#your bot token here')
