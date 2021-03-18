from discord.ext import commands , tasks 
from discord.voice_client import VoiceClient
from random import choice
import discord
import random
import os
import urllib.request
import re
import time
import asyncio
import sys
from subprocess import *
from PIL import Image ,ImageDraw ,ImageFont
import wikipedia
import wolframalpha
import subprocess
import pyttsx3
import webbrowser
import praw

client = commands.Bot(command_prefix="!")
alpha_client = wolframalpha.Client('THT5LK-UY2VW2UAK4')
status = ['Jamming out to music','Eating!','Sleeping','Chilling!']
reddit = praw.Reddit(client_id="Y4NVkEpyK-YSmA",client_secret="OlRayzfa0x8r_OUFfU7nAfy4RhCkcA",
	username="thedeadman123",password="ruwaid234",user_agent="pythonpraw")

@client.event
async def on_ready():
	change_status.start()
	print("Bot is Up !!")

@client.event
async def on_raw_reaction_add(payload):
	message_id = payload.message_id
	if message_id == 767655230782832680:
		guild_id = payload.guild_id
		guild = discord.utils.find(lambda g : g.id == guild_id , client.guilds)

		if payload.emoji.name == 'eggy':
			role = discord.utils.get(guild.roles, name='flare')
		elif payload.emoji.name == "":
			role = discord.utils.get(guild.roles, name='kind')
		else:
			role = discord.utils.get(guild.roles, name=payload.emoji.name)

		if role is not None:
			member = payload.member
			if member is not None:
				await member.add_roles(role)
				print("done")
			else:
				print("Member not found")

		else:
			print("Role not found")


 #To greet the member on joining the server
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `!help` command for details!')

#Custom_Status
@tasks.loop(seconds=10)
async def change_status():
	await client.change_presence(activity=discord.Game(choice(status)))

#Commands

 #To check the latency
@client.command(name="ping" , help="This command returns the latency")
async def ping(ctx):
	await ctx.send(f'**Pong!** Latency: {round(client.latency*1000)}ms')

@client.command()
async def runserver(ctx):
	print("Server is up!")
	Popen('python C:\\Users\\kuwai\\Desktop\\Projects\\GM\\cmd.py')
	img = Image.new('RGB', (200, 50), color = 'black')
	fnt = ImageFont.truetype('C:\\windows\\fonts\\comic.ttf', 30)
	d = ImageDraw.Draw(img)
	line= "Server is Up!"
	d.text((10,2),line,font=fnt, fill=(224, 50, 255))
	img.save("C:\\Users\\kuwai\\Desktop\\Projects\\Discord bot\\img.png")
	await ctx.send(file=discord.File("C:\\Users\\kuwai\\Desktop\\Projects\\Discord bot\\img.png"))
	os.remove("C:/Users/kuwai/Desktop/Projects/Discord bot/img.png")

 #To Chat
@client.command(name="hi" ,help="prints a random reply")
async def hi(ctx):
	msg = ['Hi', 'Pika Pika', 'Hello']
	await ctx.send(random.choice(msg))

@client.command()
async def wiki(ctx,*,values):
	results = wikipedia.summary(values, sentences=3)
	async with ctx.typing():
		await asyncio.sleep(3)
		await ctx.send('Got it.')
		await ctx.send('WIKIPEDIA says - ')
		emb = discord.Embed(description=results)
		await ctx.channel.send(embed=emb)

@client.command()
async def alpha(ctx,*,message):
	question = message
	res = alpha_client.query(question)
	results = next(res.results).text
	desp = message + '  ' + 'Answer:'+results
	emb = discord.Embed(description=desp)
	await ctx.channel.send(embed=emb)

#Bot will join voice call and play the song
@client.command(name='join', help="Plays the song in voice call")
async def join(ctx,*,message):
    channel = client.get_channel(788721223587594245)
    n = message
    path="C:\\Users\\kuwai\\Music\\Discord\\"
    file_lists=os.listdir(path)
    file_lists.sort()
    for file_list in file_lists:
    	print(file_list)

    file_name = message
    if file_name in file_lists:
    	vc = await channel.connect()
    	song = path + file_name
    	vc.play(discord.FFmpegPCMAudio(song))

@client.command()
async def song(ctx):
	path="C:\\Users\\kuwai\\Music\\Discord\\"
	file_lists=os.listdir(path)
	file_lists.sort()
	for file_list in file_lists:
		print(file_list)
		emb = discord.Embed(description=file_list)
		await ctx.channel.send(embed=emb)


 #To stop the song   		
@client.command(name='stop', help='This command stops the song!')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.stop()

 #This command pauses the song
@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()

 #This command resumes the song
@client.command(name='resume', help='This command resumes the song!')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()

 #bot will leave voice call
@client.command(name='leave', help='Bot leaves the voice call')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

 #To create poll
@client.command(name="poll",help="This command create a poll")
@commands.has_permissions(manage_messages=True)
async def poll(ctx,*,message):
	emb = discord.Embed(Title="POLL",description=f"{message}")
	msg = await ctx.channel.send(embed=emb)
	await msg.add_reaction("1️⃣"),
	await msg.add_reaction("2️⃣")

 #To clear messages sent in channel
@client.command(name="clear",help="This command clears the messages")
@commands.has_permissions(manage_messages=True)
async def clear(ctx , amount =100):
	await ctx.channel.purge(limit=amount)

def is_it_me(ctx):
	return ctx.author.id == 735899792496001096 

 #To kick someone
@client.command(name="kick" , help="kicks the member(moderators and admin only)")
@commands.has_permissions(kick_members=True)
async def kick(ctx,member : discord.Member,*,reason="Voilation of Rules"):
	await member.send("You have been kicked from the community,Due to"+reason)
	await member.kick(reason=reason)

def is_it_me(ctx):
	return ctx.author.id == 735899792496001096

 #Hmm just....nothing
@client.command(name="push" ,help='Ugh you know that!!')
@commands.has_permissions(manage_messages=True)
async def push(ctx):
	await ctx.send('Hello', file=discord.File("C:\\Users\\kuwai\\Downloads\\projectcsc.pdf"))

 #To chat
@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
  responses = [
  'why have you brought my short life to an end',
  'Okay,Let me kill someone so that i will have 500 kills.Can i kill you ',
  'i could have done so much more',
  'i have a family, kill them instead',
  'I’d hate to die twice. It’s so boring.',
  'I knew it! I knew it! Born in a hotel room and, goddamn it, dying in a hotel room.',
  'Remember, Honey, don’t forget what I told you. Put in my coffin a deck of cards, a mashie niblick, and a pretty blonde.',
  'Thank god. I’m tired of being the funniest person in the room.',
  'Oh, you young people act like old men. You have no fun.'
  ]
  await ctx.send(choice(responses))

@client.command()
async def red(ctx,message):
	subreddit = reddit.subreddit(message)
	all_subs = []
	top = subreddit.new()
	for submission in top:
		all_subs.append(submission)

	random_sub = random.choice(all_subs)
	name = random_sub.title
	url = random_sub.url

	em = discord.Embed(title=name)
	em.set_image(url=url)

	await ctx.send(url,embed=em)
@client.command()
async def em(ctx,*,message):
	emb = discord.Embed(description=f"{message}")
	await ctx.channel.purge(limit=1)
	await ctx.send(embed=emb)

@client.command()
async def createc(ctx,*,message):
	guild = ctx.message.guild
	channel = await guild.create_text_channel(message)

@client.command()
async def createv(ctx,*,message):
	guild = ctx.message.guild
	channel = await guild.create_voice_channel(message)

@client.command()
async def deletec(ctx, message):
	guild = ctx.message.guild
	existing_channel = discord.utils.get(guild.channels, name=message)
	await existing_channel.delete()

@client.command()
async def crole(ctx,message):
	guild = ctx.message.guild
	await guild.create_role(name=message)

@client.command()
async def drole(ctx,message):
	guild = ctx.message.guild
	existing_role = discord.utils.get(guild.roles, name=message)
	await existing_role.delete()


client.run("NzY2NjI1NjU0NjgxNzYzODQw.X4mFxw.7fYGIzEvhbAsDTrf3rKJ8hTIN5g")
