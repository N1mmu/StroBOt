import discord
import random
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
async def hug(ctx,arg1):
    hug_list = ['https://i2.wp.com/66.media.tumblr.com/6e54a57c5e8cd23988eabe009e0d9073/tumblr_pedx75Klrd1vh8k4yo1_500.gif','https://media.tenor.com/images/11157eb0fe0b7b0f296a8066dffa39a7/tenor.gif','https://i.imgur.com/r9aU2xv.gif','https://media0.giphy.com/media/143v0Z4767T15e/200.gif','https://i.pinimg.com/originals/bb/84/1f/bb841fad2c0e549c38d8ae15f4ef1209.gif','https://thumbs.gfycat.com/GratefulComplexGlassfrog-size_restricted.gif','https://i.imgur.com/IwaSepM.gif','https://64.media.tumblr.com/3f1e7147d4b66c14c825b538c2857f22/99d197bf411d7f84-b2/s500x750/8afe51206747d3980817cc0c23855bbdf114c555.gifv','https://i.imgur.com/v07ICwl.gif,''https://acegif.com/wp-content/gif/anime-hug-49.gif','https://acegif.com/wp-content/gif/anime-hug-38.gif','https://acegif.com/wp-content/gif/anime-hug-79.gif','https://acegif.com/wp-content/gif/anime-hug-50.gif','https://acegif.com/wp-content/gif/anime-hug-83.gif','https://acegif.com/wp-content/gif/anime-hug-73.gif','https://acegif.com/wp-content/gif/anime-hug-2.gif','https://acegif.com/wp-content/gif/anime-hug-3.gif','https://acegif.com/wp-content/gif/anime-hug-75.gif','https://pa1.narvii.com/7279/0816faa102f1e7d9b1839d788b7d0bc7dea07202r1-500-335_hq.gif','https://i.pinimg.com/originals/93/4e/91/934e9111d22518d37b9b5684fa99de79.gif','https://media.giphy.com/media/VGACXbkf0AeGs/giphy.gif','https://pa1.narvii.com/7204/d34c86981851711527fe034136747e66d79b6798r1-380-214_hq.gif','https://i.pinimg.com/originals/73/7e/3a/737e3a166fd47efd613252867a2ef437.gif','https://i.pinimg.com/originals/85/72/a1/8572a1d1ebaa45fae290e6760b59caac.gif','https://media1.tenor.com/images/f4489c22337de1d5c5a3eb20391441b1/tenor.gif?itemid=12668694','https://i0.wp.com/78.media.tumblr.com/18fdf4adcb5ad89f5469a91e860f80ba/tumblr_oltayyHynP1sy5k7wo1_500.gif?resize=650,400','https://i.pinimg.com/originals/bd/5b/0a/bd5b0ab88c4102e6a8514ffb1f0a4c0f.gif','https://64.media.tumblr.com/ce3aad3f1d570fa06c253abfccf36d1b/tumblr_msexao8iX51re6rdoo1_500.gif','https://media1.tenor.com/images/d349db7108547e020d54c40fc560091e/tenor.gif?itemid=11735639','https://i.pinimg.com/originals/2d/22/63/2d226391814aa2ae0032cebd5745dc0f.gif','https://i.redd.it/1axsapcx3jy11.gif']
    embed = discord.Embed(
        #title =' ',
      description ='{} ** ,you have been hugged by ** {}'.format(arg1,ctx.message.author.name),
      colour = discord.Colour.blue()
    )
    embed.set_image(url=random.choice(hug_list))
    embed.set_footer(text='Kawaii~')
    await ctx.send(embed=embed)

@client.command()
async def kiss(ctx,arg1):
    kiss_list =['https://steamuserimages-a.akamaihd.net/ugc/882005587667465433/0C4C638277B865B1C228FAA3E06DEA6672431633/','https://cutewallpaper.org/21/kiss-in-anime/Anime-Kissing-GIF-Anime-Kissing-Kiss-Discover-and-Share-GIFs.gif','https://64.media.tumblr.com/888faa007b704b23bf703d8ab2b49be1/tumblr_odt1gwmZNG1t86l7wo1_500.gifv','https://media1.tenor.com/images/d0cd64030f383d56e7edc54a484d4b8d/tenor.gif?itemid=17382422','https://i.gifer.com/8Sbz.gif','https://media1.tenor.com/images/1e17e602bc2ef91fd18e1fe23dd664dd/tenor.gif?itemid=17914573','https://64.media.tumblr.com/5d51b3bbd64ccf1627dc87157a38e59f/tumblr_n5rfnvvj7H1t62gxao1_500.gif','https://www.icegif.com/wp-content/uploads/anime-kiss-icegif-1.gif','https://media1.tenor.com/images/be8014584d3ed6e29b43a2044503b90b/tenor.gif?itemid=10358836','https://media1.tenor.com/images/271a3ea782865b00ad6dc54d391d6eb8/tenor.gif?itemid=10356308','https://thumbs.gfycat.com/HopefulFabulousKouprey-size_restricted.gif','https://media1.tenor.com/images/7e28715f3c114dc720688f1a03abc5f5/tenor.gif?itemid=5463442','https://media.tenor.com/images/197df534507bd229ba790e8e1b5f63dc/tenor.gif','https://i1.wp.com/novocom.top/image/bG92Z5hbWUWlzYW5hbWUuY29t/wp-content/uploads/2016/09/23.gif','https://i.pinimg.com/originals/41/6a/85/416a8536c3ba7830c64cd9847e3b880d.gif','https://i.pinimg.com/originals/8d/f2/c3/8df2c3933127d6c7cd8f66d1347a773b.gif','https://acegif.com/wp-content/uploads/anime-kiss-8.gif','https://monophy.com/media/QGc8RgRvMonFm/monophy.gif','https://i.pinimg.com/originals/66/19/1b/66191b81d5bf6c70bd065736f3e8662b.gif','https://data.whicdn.com/images/320446353/original.gif','https://media1.tenor.com/images/187afb381a1529f07e16afc484af5b40/tenor.gif?itemid=16685588','https://64.media.tumblr.com/867584ae83cdaca2064bec258c197dc1/tumblr_mggon6vDQJ1s2n3h7o1_500.gif','https://64.media.tumblr.com/c875c6a63546a08a850dba0a04a18260/tumblr_inline_nq0duvrhNx1sjmrlk_400.gifv','https://data.whicdn.com/images/199257401/original.gif','https://media1.tenor.com/images/37633f0b8d39daf70a50f69293e303fc/tenor.gif?itemid=13344412','https://media1.tenor.com/images/30e9b0b2a07304a448d263b4c91938aa/tenor.gif?itemid=13908226','https://cutewallpaper.org/21/anime-hot-kiss/Animated-gif-about-kiss-in-anime-by-julie-in-many-ways.gif','https://64.media.tumblr.com/162fae92689e51b35946e11af62619be/tumblr_mtj3c1HsKK1s9pzh1o1_500.gif','https://i.pinimg.com/originals/81/d2/8b/81d28b84bab0eb5c7e54c64e3fe2f82f.gif','https://i.gifer.com/36KV.gif','https://i.gifer.com/ByGm.gif','https://i0.wp.com/gifimage.net/wp-content/uploads/2017/09/anime-couple-kissing-gif-14.gif','https://i.pinimg.com/originals/10/5a/7a/105a7ad7edbe74e5ca834348025cc650.gif','https://i.pinimg.com/originals/02/88/71/028871291e7863a63a169321943737be.gif','https://i1.wp.com/66.media.tumblr.com/83cc6360fa4a87ce54b8dae3113b5443/tumblr_pgwxu4iKtZ1w9n1na_400.gif','https://s11.favim.com/orig/7/716/7160/71608/ichigo-anime-couple-kiss-Favim.com-7160874.gif','https://i.kym-cdn.com/photos/images/newsfeed/001/372/173/dea.gif','https://thumbs.gfycat.com/ImpressiveShockedArabianhorse-max-1mb.gif']
    

    embed = discord.Embed(
      #title =' ',
      description ='{} ** you have been kissed by ** {}'.format(arg1,ctx.message.author.name),
      colour = discord.Colour.blue()
    )
    embed.set_image(url=random.choice(kiss_list))
    embed.set_footer(text='Kawaii~')
    await ctx.send(embed=embed)

@client.command()
async def cuddle(ctx,arg1):
    cuddle_list = ['https://thumbs.gfycat.com/MealyWellinformedDassierat-max-1mb.gif','https://i.pinimg.com/originals/f1/f7/7d/f1f77dc0c5ef8166c51c3e8b80556d98.gif','https://i.pinimg.com/originals/d8/7c/5c/d87c5cdd0a68caf2b6feeec0f7da7315.gif','https://acegif.com/wp-content/gif/anime-hug-86.gif','https://64.media.tumblr.com/d04f4461f117c3b8d7a8f23796358a15/tumblr_nberq3XV2M1t5l0ico1_500.gif','https://i.kym-cdn.com/photos/images/newsfeed/000/987/510/f81.gif','https://data.whicdn.com/images/253502283/original.gif','https://i.kym-cdn.com/photos/images/original/001/230/145/957.gif','https://64.media.tumblr.com/tumblr_ma7l17EWnk1rq65rlo1_500.gif','https://img.wattpad.com/0f7be27441deca292b8abf474687d155e00df0ce/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f573373443971664a6f41675651513d3d2d3537393931333635382e313533323163663734326132653861323530373835303437393934352e676966','https://i.kym-cdn.com/photos/images/original/001/153/417/104.gif','https://media1.tenor.com/images/6d73b0a9cadef5310be4b6160d2f959a/tenor.gif?itemid=12099823','https://steamuserimages-a.akamaihd.net/ugc/449584613101112607/4FEFF66AC3E64721E0B50E79BFB807436BB64A75/','https://archive.nyafuu.org/foolfuuka/boards/c/image/1536/35/1536356307236.gif','https://img.wattpad.com/2db78027df7e671b419ba34ece95f689b5c3045b/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f4c6a4e31775545304379417730773d3d2d3837323930383836352e3136303866653234663534303538356239373635373430363836382e676966']
    embed = discord.Embed(
      #title =' ',
      description ='AWWW {} ** , Here is your cuddle from ** {}'.format(arg1,ctx.author.mention),
      colour = discord.Colour.blue()
    )
    embed.set_image(url=random.choice(cuddle_list))
    embed.set_footer(text='warm~')
    await ctx.send(embed=embed)

@client.command()
async def makeout(ctx,arg1):
    makeover_list = ['https://steamuserimages-a.akamaihd.net/ugc/882005587667465433/0C4C638277B865B1C228FAA3E06DEA6672431633/','https://media1.giphy.com/media/G3va31oEEnIkM/giphy.gif?cid=790b7611a92f0d31a957dfdb015006bd009dd1953aa03514&rid=giphy.gif&ct=g','https://media1.tenor.com/images/34ecc943dd11f0c55689e25f1bacddfb/tenor.gif?itemid=14816388','https://i.pinimg.com/originals/5e/1e/8c/5e1e8c81c01a1e26db4c0e18ae8bafd5.gif','https://64.media.tumblr.com/32961c313ac0e9095425772eb2a08897/tumblr_mximpwMA6p1t2wbmao1_500.gif','https://media1.tenor.com/images/b5109a90cc400e53526bfd0917194cf6/tenor.gif?itemid=15979384','https://thumbs.gfycat.com/DishonestSentimentalHornet-size_restricted.gif','https://cutewallpaper.org/21/anime-passionate-kiss/Anime-Scums-Wish-GIF-Anime-ScumsWish-Passionate-Discover-Share-GIFs.gif','https://media1.tenor.com/images/1b0387dd493e3d58915fa9814764412b/tenor.gif?itemid=17082696','https://media1.tenor.com/images/58e8a1cc917ee23ccdeba0fd253a3ea3/tenor.gif?itemid=11792978','https://64.media.tumblr.com/00ab484ca02a77b880d7009cc35d3cd3/tumblr_n526hnMfML1tag3fyo1_500.gif','https://i.pinimg.com/originals/33/7b/24/337b24eb2475b769057e4c0e552c0835.gif','https://i.pinimg.com/originals/14/ef/e0/14efe06fce2e1917c659e95a7a4542ef.gif']
   

    embed = discord.Embed(
      #title =' ',
      description ='Ara Ara {} ** ,You have tasted ** {} :eyes:'.format(arg1,ctx.author.mention),
      colour = discord.Colour.blue()
    )
    embed.set_image(url=random.choice(makeover_list))
    embed.set_footer(text='Yummyyyy~')
    await ctx.send(embed=embed)

@client.command()
async def sleep(ctx,arg1):
    sleep_list = ['https://media.tenor.com/images/69f015303c94bc9c35aba4e8eef4be5e/tenor.gif','https://data.whicdn.com/images/249663938/original.gif','https://cutewallpaper.org/21/anime-cute-kiss/Anime-Kiss-GIFs-Tenor.gif','https://thumbs.gfycat.com/BlushingDeepBlacknorwegianelkhound-size_restricted.gif']
    embed = discord.Embed(
      #title =' ',
      description ='Good night'.format(arg1,ctx.author.mention),
      colour = discord.Colour.blue()
    )
    embed.set_image(url=random.choice(sleep_list))
    embed.set_footer(text='sleep well~')
    await ctx.send(embed=embed)

@client.command()
async def shoulder(ctx,arg1):
    shoulder_list = ['https://giffiles.alphacoders.com/133/133140.gif','https://data.whicdn.com/images/220089647/original.gif']
    embed = discord.Embed(
      #title =' ',
      description ='{} has rested on {} shoulder '.format(ctx.author.mention,arg1),
      colour = discord.Colour.blue()
    )
    embed.set_image(url=random.choice(shoulder_list))
    embed.set_footer(text='comfyyy~')
    await ctx.send(embed=embed)
    
@client.command()
async def smile(ctx,arg1):
    smile_list = ['https://animemotivation.com/wp-content/uploads/2021/04/golden-time-couple-gif.gif','https://data.whicdn.com/images/80411925/original.gif','https://64.media.tumblr.com/cc893a0ee40d73d083da3df4bdaf45cc/tumblr_mu4k3hWcRB1rydwbvo1_500.gifv','https://i.pinimg.com/originals/da/9a/48/da9a4871139cc41087b2575ddde77fd8.gif','https://i0.wp.com/media1.tenor.com/images/faf9e8b4615bb2d3d3e79d3bd8b6353f/tenor.gif','https://i.kym-cdn.com/photos/images/newsfeed/000/771/828/b9b']
    embed = discord.Embed(
      #title =' ',
      description ='Awww.. you both look cute :) ',
      colour = discord.Colour.blue()
    )
    embed.set_image(url=random.choice(smile_list))
    embed.set_footer(text='kawaii~')
    await ctx.send(embed=embed)

@client.command()
async def lick(ctx,arg1):
    lick_list = ['https://lh3.googleusercontent.com/proxy/uMdQrsA5LKqGU90f9bFP5PcvZrYxj4s_VlJYav_z6lPuf41Tuea_yE3gnrSBZr5-K3MGsW7ywc-m4IBFoITm2OkNAM9QMFH37kItGsp0Gb0eFQ','https://image.myanimelist.net/ui/bfln5jRa_L37ziNWm-xNvGXgBcL8JbIiOhbt7nNfaeWFk3_IBNpcdkRpxmPoR6TPBvE4kcdHf2KA_l7R2zf-ioYSgDzh8mgl3qiahmC6rH0','https://i.redd.it/d0cwk8ixw6271.gif','https://i.kym-cdn.com/photos/images/original/001/230/497/04d.gif','https://media1.tenor.com/images/c4f68fbbec3c96193386e5fcc5429b89/tenor.gif?itemid=13451325']
    embed = discord.Embed(
      #title =' ',
      description ='sloop :eyes:... {} you have been licked'.format(arg1),
      colour = discord.Colour.blue()
    )
    embed.set_image(url=random.choice(lick_list))
    embed.set_footer(text=' :eyes: ~')
    await ctx.send(embed=embed)

#@client.command()
#async def secret(ctx,arg1):
  #if 1==1:
    #author = '{}'.format(ctx.author.mention)
    #author = "{}".format(ctx.message.author.name)
    #if 1==1:
      #n_secret_list = ['https://ahegao.b-cdn.net/wp-content/uploads/2020/06/diabolik-lovers.gif']
      #embed = discord.Embed(
        #title =' ',
        #description =':eyes:'.format(arg1),
        #colour = discord.Colour.blue()
      #)
      #embed.set_image(url=random.choice(n_secret_list))
      #embed.set_footer(text=' :eyes: ~')
    #await ctx.send(embed=embed)
    #await ctx.send(author)

  #else:
   #await ctx.send("this is a secret command only useable by the dev for a certain someone :eyes:")

@client.command()
async def pat(ctx,arg1):
    pat_list = ['https://c.tenor.com/E6fMkQRZBdIAAAAM/kanna-kamui-pat.gif','https://c.tenor.com/dmYhPDHbbI4AAAAM/misha-misha-necron-anos-voldigoad-the-misfit-of-demon-king-academy-headpat-pat.gif','https://i.pinimg.com/originals/ba/0a/18/ba0a18b4028f9c210f830f7a82a574cb.gif','https://66.media.tumblr.com/a72dd82535f3e7accd827c202dacc09a/tumblr_pfyiqz0pFL1th206io1_640.gif','https://c.tenor.com/wLqFGYigJuIAAAAC/mai-sakurajima.gif','https://c.tenor.com/GC9rg-v-wvMAAAAC/anime-pat.gif','https://i.pinimg.com/originals/c2/23/2a/c2232aec426d8b5e85e026cbca410463.gif','https://thumbs.gfycat.com/EnchantingObedientGermanspitz-max-1mb.gif','https://i.imgur.com/pb0ODYa.gif','https://image.myanimelist.net/ui/OK6W_koKDTOqqqLDbIoPAjOymhqy8UFF3k45tZQWUuc','https://thumbs.gfycat.com/BlankGiftedBurro-size_restricted.gif','https://i.pinimg.com/originals/30/e3/db/30e3dbf4ec1bf8c8910d8658d18fba52.gif','https://media.giphy.com/media/l3vRaaB8exIXg4J9u/giphy.gif','https://c.tenor.com/QAIyvivjoB4AAAAC/anime-anime-head-rub.gif']
    embed = discord.Embed(
      #title =' ',
      description ='{} , you have been patted by {} '.format(arg1,ctx.author.mention),
      colour = discord.Colour.blue()
    )
    embed.set_image(url=random.choice(pat_list))
    embed.set_footer(text='patto patto~')
    await ctx.send(embed=embed)
    
@client.command()
async def holdhands(ctx,arg1):
    hand_list = ['https://s12.favim.com/gif_previews/7/787/7878/78787/7878763.gif','https://64.media.tumblr.com/7a1d87c8e7056ac5ce2a202d53a36905/tumblr_myqbqfZWSb1sp0cggo1_500.gif','https://c.tenor.com/WUZAwo5KFdMAAAAC/love-holding-hands.gif','https://c.tenor.com/rU3xZo2_jaIAAAAC/anime-hold.gif','https://c.tenor.com/NuDEahFzxokAAAAC/love-hold-hands.gif','https://i.pinimg.com/originals/b9/7c/3b/b97c3bf7842833f7a735db8df9503eec.gif','https://i.pinimg.com/originals/f1/c1/0a/f1c10af3018241ecd34c30581f94c49e.gif','https://64.media.tumblr.com/9f591aed456adfd0ed6d1619e3d08dfa/a943f0088f9398e4-d3/s1280x1920/0072a0d2ebd3473d744c48e55610078ac57236d4.gifv','https://64.media.tumblr.com/8d0a98150637c40bfd9d782a4314e3a0/tumblr_p86198mRIY1uwpz4ao2_500.gif']
    embed = discord.Embed(
      #title =' ',
      description ='{} , tells you to stop worrying {} '.format(ctx.author.mention,arg1),
      colour = discord.Colour.blue()
    )
    embed.set_image(url=random.choice(hand_list))
    embed.set_footer(text='smileeee plsss~')
    await ctx.send(embed=embed)
 
@client.command()
async def tickle(ctx,arg1):
    tickle_list = ['https://c.tenor.com/L5-ABrIwrksAAAAC/tickle-anime.gif','https://64.media.tumblr.com/1bf8a604284b2e84c37e399f0b0d20d9/tumblr_o7svtzsXDE1vpbklao4_500.gifv','https://64.media.tumblr.com/b6406e8acd03a03f83b55db5082fcad7/tumblr_ohs63qIx0R1vpbklao1_500.gifv','https://c.tenor.com/PXL1ONAO9CEAAAAC/tickle-laugh.gif','https://i.imgur.com/VD8nvU5.gif','https://64.media.tumblr.com/c78f078c919131ebce3c47b0ab609f01/tumblr_oammb542dO1vpbklao1_500.gifv','https://j.gifs.com/Kdla3Y.gif','http://pa1.narvii.com/5997/284518131a267b5641cc6f3f9618da18466406e4_hq.gif']
    embed = discord.Embed(
      #title =' ',
      description ='{} , you got tickled by {} '.format(arg1,ctx.author.mention),
      colour = discord.Colour.purple()
    )
    embed.set_image(url=random.choice(tickle_list))
    embed.set_footer(text='Kichikichi😂~')
    await ctx.send(embed=embed)

@client.command()
async def buttrub(ctx,arg1):
    buttrub_list = ['https://c.tenor.com/zdzCWH3WiDsAAAAd/booty-rub-cute.gif','https://c.tenor.com/dpYsHnHqgekAAAAC/booty-rub-smiling.gif','https://c.tenor.com/ay5SfMh39JUAAAAj/massage-body.gif','https://c.tenor.com/sdvuTXU1EIEAAAAi/quby-cute.gif','https://c.tenor.com/7S3hEvXkVi8AAAAC/massaging-pat.gif','https://c.tenor.com/ZOK7f3f_MOgAAAAC/bootyrub-booty.gif','https://c.tenor.com/54IzCek9UBoAAAAC/cute-couple-massage.gif','https://c.tenor.com/sb2aDjBRrFwAAAAC/cats-massage.gif']
    embed = discord.Embed(
      #title =' ',
      description ='{} , here is your buttrub from {} '.format(arg1,ctx.author.mention),
      colour = discord.Colour.purple()
    )
    embed.set_image(url=random.choice(buttrub_list))
    embed.set_footer(text='🙃')
    await ctx.send(embed=embed)
    

@client.command()
async def delete(ctx):
        await ctx.channel.delete()
        new_channel = await ctx.channel.clone(reason="Channel was purged")
        await new_channel.edit(position=ctx.channel.position)
        await new_channel.send("Channel was purged")



client.run('ODkwMjg5NDI5NTczNDI3Mjky.YUtopA.kvJ9Jzlw0hZwfSWUBSuxwqYqntk')
