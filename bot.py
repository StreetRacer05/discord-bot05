import discord
from discord.ext import commands

client = commands.Bot( command_prefix = '!' )
client.remove_command( 'help' )


@client.command( pass_context = True )

async def hello( ctx ):
	author = ctx.message.author

	await ctx.send( f' { author.mention } Hello. I am a BOT for discord from Wargaming' )

#Words
hello_words = ( 'hello', 'hi', 'привет', 'здарова', 'ky', 'privet', 'даров', 'хеллоу', 'хелоу' )
goodbye_words = ( 'bb', 'пока', 'poka', 'покеда', 'pokeda', 'бай' )
slava_words = ( 'Слава Украине', 'слава украине', 'Slava Ukraine', 'Украине Слава', 'украине слава', 'СЛАВА УКРАИНЕ', 'slava ukraine', 'Слава Украине!' )





@client.event 

async def on_ready():
	print( 'BOT connected' )

@client.event

async def on_message(message):
	await client.process_commands(message)
	msg = message.content.lower()

	if msg in hello_words:
		await message.channel.send( 'Привет, иди нахуй.' )

	if msg in goodbye_words:
		await message.channel.send( 'Ну и вали, бомж блять' )
	if msg in slava_words:
		await message.channel.send( 'Героям Слава!' )


#clear message
@client.command( pass_context = True )
async def clear( ctx, amount = 100 ):
	await ctx.channel.purge( limit = amount )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )



#kick
@commands.has_permissions ( administrator = True )
async def kick(ctx, member:discord.Member,*,reason = None):
	await ctx.channel.purge(limit = 1)
	await member.kick(reason = reason)
	await ctx.send(f'kick user { member.mention }')


#ban
@client.command( pass_context = True )
@commands.has_permissions(administrator = True)
async def ban(ctx,member:discord.Member,*,reason = None):
	await ctx.channel.purge( limit = 1  )
	await member.ban( reason = reason )
	await ctx.send( f'ban user { member.mention }' )
# Command help
@client.command( pass_context = True )
async def help( ctx ):
	emb = discord.Embed( title = 'Список доступных команд' )

	emb.add_field( name = 'clear', value = 'Очистка чата от сообщений' )
	emb.add_field( name = 'kick', value = 'Кик участника' )
	emb.add_field( name = 'ban' , value = 'Бан участника' )
	emb.add_field( name = 'mute', value = 'Мут участника' )

	await ctx.send( embed = emb )


@client.command()
@commands.has_permissions(administrator = True)
async def mute(ctx, member:discord.Member):
	await ctx.channel.purge(limit = 1)

	mute_role = discord.utils.get(ctx.message.guild.roles,name = 'Mute')

	await member.add_roles(mute_role)
	await ctx.send(f'{member.mention}, Попал в мут на этом сервере')

# Connect

token = 'NzA3Mjk4OTE2Njc2NDAzMjkw.XrKDrA.qQaWMSxX3kqOO6uH7tu3lzpor44'

client.run ( token )