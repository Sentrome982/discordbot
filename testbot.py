import discord.ext
from discord.utils import get
import discord

client = commands.Bot(command_prefix = "//", help_command=None)

@client.event
async def on_ready():
    print(f"{client.user} has Awoken!")

@client.command()
async def test(ctx):
    Admin = get(ctx.guild.roles, name="Admin")
    clvrk = get(ctx.guild.members, name="clvrk")
    await ctx.send(f"Admin role:\n{Admin.mention}\n\n Clark:\n{clvrk.mention}")

client.run("ODI1NTYxNzAyNjY5MzUyOTYw.YF_uQA.XLQAPb7p25_YhrMj-x_k2lMvyJg")