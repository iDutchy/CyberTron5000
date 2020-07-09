import asyncio
import random

import discord
from async_timeout import timeout
from discord.ext import commands

colour = 0x00dcff


class Games(commands.Cog):
    """Games!"""
    
    def __init__(self, client):
        self.client = client
    
    # rock paper scissors, shoot

    @commands.command(aliases=['rps'], help="Rock paper scissors shoot")
    async def rockpaperscissors(self, ctx):
        # an outcome of 0 is a win, 1 is a draw and 2 is  a loss.
        choice = random.choice(['rock', 'paper', 'scissors'])
        embed = discord.Embed(colour=colour, description="**Choose one** :point_down:")
        msg = await ctx.send("** **", embed=embed)
        for e in ['🗿', '✂']:
            await msg.add_reaction(e)
            await msg.add_reaction(emoji="📄")
        async with timeout(30):
            reaction, user = await self.client.wait_for(
                'reaction_add',
                timeout=30.0,
                check=lambda reaction,
                             user: reaction.emoji
            )
        
            if str(reaction.emoji) == "🗿":
                if choice == 'scissors':
                    final_outcome = 0
                else:
                    final_outcome = 1 if choice == 'rock' else 2
            elif str(reaction.emoji) == "📄":
                if choice == 'rock':
                    final_outcome = 0
                else:
                    final_outcome = 1 if choice == 'paper' else 2
            elif str(reaction.emoji) == "✂":
                if choice == 'paper':
                    final_outcome = 0
                else:
                    final_outcome = 1 if choice == 'scissors' else 2
            if not final_outcome:
                await msg.edit(embed=discord.Embed(colour=colour).set_author(name=f"You won! I drew {choice}!"))
            else:
                await msg.edit(embed=discord.Embed(colour=colour).set_author(
                    name=f"You lost! I drew {choice}!")) if final_outcome == 2 else await msg.edit(
                    embed=discord.Embed(colour=colour).set_author(name=f"It was a draw! We both drew {choice}!"))
    
    # kiss marry kill command
    
    @commands.command(help="Kiss, marry, kill.", aliases=['kmk'])
    async def kissmarrykill(self, ctx):
        member1 = random.choice(ctx.guild.members)
        member2 = random.choice(ctx.guild.members)
        member3 = random.choice(ctx.guild.members)
        if member1 == member2:
            member1 = random.choice(ctx.guild.members)
        elif member3 == member2:
            member3 = random.choice(ctx.guild.members)
        embed = discord.Embed(colour=colour,
                              description=f"**Would you kiss (😘), marry (👫), or kill(🔪) {member1.display_name}?**")
        embed.add_field(name=member1.display_name, value="\u200b")
        embed.add_field(name=member2.display_name, value="\u200b")
        embed.add_field(name=member3.display_name, value="\u200b")
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        msg = await ctx.send(embed=embed)
        for emoji in ['😘', '🔪']:
            await msg.add_reaction(emoji)
            await msg.add_reaction(emoji='👫')
        async with timeout(30):
            reaction, user = await self.client.wait_for(
                'reaction_add',
                timeout=30.0,
                check=lambda reaction,
                             user: reaction.emoji
            )
            if str(reaction.emoji) == "😘":
                
                embed1 = discord.Embed(colour=colour,
                                       description=f"**Would you marry (👫), or kill(🔪) {member2.display_name}?**")
                embed1.add_field(name=member1.display_name, value="😘")
                embed1.add_field(name=member2.display_name, value="\u200b")
                embed1.add_field(name=member3.display_name, value="\u200b")
                embed1.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
                msg1 = await ctx.send(embed=embed1)
                await msg1.add_reaction(emoji='👫')
                await msg1.add_reaction(emoji="🔪")
                await asyncio.sleep(0.1)
                async with timeout(30):
                    reaction, user = await self.client.wait_for(
                        'reaction_add',
                        timeout=30.0,
                        check=lambda reaction,
                                     user: reaction.emoji
                    )
                    if str(reaction.emoji) == "👫":
                        
                        embed2 = discord.Embed(colour=colour,
                                               description=f"**Results**")
                        embed2.add_field(name=member1.display_name, value="😘")
                        embed2.add_field(name=member2.display_name, value="👫")
                        embed2.add_field(name=member3.display_name, value="🔪")
                        embed2.set_author(name=ctx.message.author.display_name,
                                          icon_url=ctx.message.author.avatar_url)
                        await ctx.send(embed=embed2)
                    elif str(reaction.emoji) == "🔪":
                        
                        embed2 = discord.Embed(colour=colour,
                                               description=f"**Results**")
                        embed2.add_field(name=member1.display_name, value="😘")
                        embed2.add_field(name=member2.display_name, value="🔪")
                        embed2.add_field(name=member3.display_name, value="👫")
                        embed2.set_author(name=ctx.message.author.display_name,
                                          icon_url=ctx.message.author.avatar_url)
                        await ctx.send(embed=embed2)
            elif str(reaction.emoji) == "👫":
                
                embed1 = discord.Embed(colour=colour,
                                       description=f"**Would you kiss (😘), or kill(🔪) {member2.display_name}?**")
                embed1.add_field(name=member1.display_name, value="👫")
                embed1.add_field(name=member2.display_name, value="\u200b")
                embed1.add_field(name=member3.display_name, value="\u200b")
                embed1.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
                msg1 = await ctx.send(embed=embed1)
                for e in ['🔪']:
                    await msg1.add_reaction(e)
                await msg1.add_reaction(emoji='😘')
                await asyncio.sleep(0.1)
                async with timeout(30):
                    reaction, user = await self.client.wait_for(
                        'reaction_add',
                        timeout=30.0,
                        check=lambda reaction,
                                     user: reaction.emoji
                    )
                    if str(reaction.emoji) == "😘":
                        
                        embed2 = discord.Embed(colour=colour,
                                               description=f"**Results**")
                        embed2.add_field(name=member1.display_name, value="👫")
                        embed2.add_field(name=member2.display_name, value="😘")
                        embed2.add_field(name=member3.display_name, value="🔪")
                        embed2.set_author(name=ctx.message.author.display_name,
                                          icon_url=ctx.message.author.avatar_url)
                        await ctx.send(embed=embed2)
                    elif str(reaction.emoji) == "🔪":
                        
                        embed2 = discord.Embed(colour=colour,
                                               description=f"**Results**")
                        embed2.add_field(name=member1.display_name, value="👫")
                        embed2.add_field(name=member2.display_name, value="🔪")
                        embed2.add_field(name=member3.display_name, value="😘")
                        embed2.set_author(name=ctx.message.author.display_name,
                                          icon_url=ctx.message.author.avatar_url)
                        await ctx.send(embed=embed2)
            elif str(reaction.emoji) == "🔪":
                
                embed1 = discord.Embed(colour=colour,
                                       description=f"**Would you kiss (😘), or marry (👫) {member2.display_name}?**")
                embed1.add_field(name=member1.display_name, value="🔪")
                embed1.add_field(name=member2.display_name, value="\u200b")
                embed1.add_field(name=member3.display_name, value="\u200b")
                embed1.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
                msg1 = await ctx.send(embed=embed1)
                await msg1.add_reaction(emoji='😘')
                await msg1.add_reaction(emoji='👫')
                await asyncio.sleep(0.1)
                async with timeout(30):
                    reaction, user = await self.client.wait_for(
                        'reaction_add',
                        timeout=30.0,
                        check=lambda reaction,
                                     user: reaction.emoji
                    )
                    if str(reaction.emoji) == "😘":
                        
                        embed2 = discord.Embed(colour=colour,
                                               description=f"**Results**")
                        embed2.add_field(name=member1.display_name, value="🔪")
                        embed2.add_field(name=member2.display_name, value="😘")
                        embed2.add_field(name=member3.display_name, value="👫")
                        embed2.set_author(name=ctx.message.author.display_name,
                                          icon_url=ctx.message.author.avatar_url)
                        await ctx.send(embed=embed2)
                    elif str(reaction.emoji) == "👫":
                        
                        embed2 = discord.Embed(colour=colour,
                                               description=f"**Results**")
                        embed2.add_field(name=member1.display_name, value="🔪")
                        embed2.add_field(name=member2.display_name, value="👫")
                        embed2.add_field(name=member3.display_name, value="😘")
                        embed2.set_author(name=ctx.message.author.display_name,
                                          icon_url=ctx.message.author.avatar_url)
                        
                        await ctx.send(embed=embed2)


def setup(client):
    client.add_cog(Games(client))
