import json
import os

import discord
from discord.ext import commands
from CyberTron5000.CyberTron5000.cogs.utils.checks import check_admin_or_owner

colour = 0x00dcff


async def get_prefix(client, message):
    with open("CyberTron5000/CyberTron5000/prefixes.json", "r") as f:
        data = json.load(f)
    if message.guild:
        try:
            pref = str(data[str(message.guild.id)])
            command_prefix = commands.when_mentioned_or(pref)(client, message)
        except KeyError:
            command_prefix = commands.when_mentioned_or("=")(client, message)
        return command_prefix
    else:
        return "="


client = commands.Bot(command_prefix=get_prefix, pm_help=None)
client.remove_command('help')


@client.event
async def on_guild_join(guild):
    with open("CyberTron5000/CyberTron5000/prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "="
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open("CyberTron5000/CyberTron5000/prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@client.group(invoke_without_command=True, help="Change the guild's prefix", aliases=['prefix', 'pre'])
@check_admin_or_owner()
async def changeprefix(ctx, *, prefix):
    with open("CyberTron5000/CyberTron5000/prefixes.json", "r") as f:
        prefixes = json.load(f)
    
    prefixes[str(ctx.guild.id)] = prefix
    
    with open("CyberTron5000/CyberTron5000/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    await ctx.message.add_reaction(emoji=":GreenTick:707950252434653184")
    await ctx.guild.me.edit(nick=f"({prefix}) {client.user.name}")


@changeprefix.command(invoke_without_command=True, help="Make your prefix end in a space.", aliases=['sp'])
@check_admin_or_owner()
async def spaceprefix(ctx, *, prefix):
    with open("CyberTron5000/CyberTron5000/prefixes.json", "r") as f:
        prefixes = json.load(f)
    
    prefixes[str(ctx.guild.id)] = f"{prefix} "
    
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    await ctx.message.add_reaction(emoji=":GreenTick:707950252434653184")
    await ctx.guild.me.edit(nick=f"({prefix}) {client.user.name}")


@client.event
async def on_ready():
    print("online!")
    for filename in os.listdir('CyberTron5000/CyberTron5000/cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
    print("Online!")
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening,
                                  name=f"{len(client.users):,} users in {len(client.guilds):,} guilds"))


@client.group(invoke_without_command=True)
async def owner(ctx, *, idea):
    """Suggest an idea for the bot."""
    owner = client.get_user(id=350349365937700864)
    await owner.send(f"Idea: ```{idea}```")
    await ctx.message.add_reaction(emoji=":GreenTick:707950252434653184")


@owner.command(invoke_without_command=True)
async def error(ctx, *, error):
    """Report an error for this bot."""
    owner = client.get_user(id=350349365937700864)
    await owner.send(f"You should fix ```{error}```")
    await ctx.message.add_reaction(emoji=":GreenTick:707950252434653184")


@client.command(help="Loads Cogs.")
@commands.is_owner()
async def load(ctx, extension=None):
    if not extension:
        for filename in os.listdir('CyberTron5000/CyberTron5000/cogs'):
            if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
        
        await ctx.send("\n".join(
            [f":arrow_up: `cogs.{f[:-3]}`" for f in os.listdir('CyberTron5000/CyberTron5000/cogs') if
             f.endswith(".py")]))
    
    else:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f":arrow_up: `cogs.{extension}`")


@client.command(help="Unloads Cogs.")
@commands.is_owner()
async def unload(ctx, extension=None):
    if not extension:
        for filename in os.listdir('CyberTron5000/CyberTron5000/cogs'):
            if filename.endswith('.py'):
                client.unload_extension(f'cogs.{filename[:-3]}')
        
        await ctx.send("\n".join(
            [f":arrow_down: `cogs.{f[:-3]}`" for f in os.listdir('CyberTron5000/CyberTron5000/cogs') if
             f.endswith(".py")]))
    
    else:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f":arrow_down: `cogs.{extension}`")


@client.command(help="Reloads Cogs")
@commands.is_owner()
async def reload(ctx, extension=None):
    if not extension:
        for filename in os.listdir('CyberTron5000/CyberTron5000/cogs'):
            if filename.endswith('.py'):
                client.reload_extension(f'cogs.{filename[:-3]}')
        
        await ctx.send("\n".join(
            [f":repeat: `cogs.{f[:-3]}`" for f in os.listdir('CyberTron5000/CyberTron5000/cogs') if f.endswith(".py")]))
    
    else:
        client.reload_extension(f'cogs.{extension}')
        await ctx.send(f":repeat: `cogs.{extension}`")

# yeet yeet yeet 1995