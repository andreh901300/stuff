#!/usr/bin/env python3
"""
a little discord bot with a handful of fun commands.

setup:
  1. pip install -r requirements.txt   (or the repo's top-level one)
  2. make a bot at https://discord.com/developers/applications
  3. copy .env.example to .env and paste your token in
  4. python3 bot.py

commands (prefix "!"):
  !ping                 -> pong + latency
  !roll 3d6+2           -> roll dice
  !flip                 -> coin flip
  !8ball <question>     -> magic 8 ball
  !choose a | b | c     -> pick one
  !say <text>           -> echo back (and delete your message)
  !avatar [@user]       -> show someone's avatar
  !userinfo [@user]     -> basic info about a user
  !help                 -> this list
"""
import os
import random
import re

import discord
from discord.ext import commands

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    # dotenv is optional; env vars still work without it
    pass

PREFIX = os.getenv("BOT_PREFIX", "!")

intents = discord.Intents.default()
intents.message_content = True  # needed for prefix commands
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

EIGHT_BALL = [
    "yes", "no", "maybe", "absolutely", "lmao no", "ask again later",
    "signs point to yes", "doubt it", "100%", "outlook not so good",
]


@bot.event
async def on_ready():
    print(f"logged in as {bot.user} (id: {bot.user.id})")
    print(f"serving {len(bot.guilds)} guild(s). prefix is {PREFIX!r}")


@bot.command()
async def ping(ctx):
    """pong + websocket latency"""
    await ctx.send(f"🏓 pong! `{round(bot.latency * 1000)}ms`")


@bot.command()
async def roll(ctx, spec: str = "1d20"):
    """roll dice like 3d6+2"""
    m = re.fullmatch(r"(\d*)d(\d+)([+-]\d+)?", spec.lower())
    if not m:
        await ctx.send("couldn't read that. try like `!roll 3d6+2`")
        return
    count = int(m.group(1) or 1)
    sides = int(m.group(2))
    mod = int(m.group(3)) if m.group(3) else 0
    if not (1 <= count <= 100) or sides < 1:
        await ctx.send("keep it reasonable please (1-100 dice)")
        return
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls) + mod
    detail = " + ".join(map(str, rolls))
    if mod:
        detail += f" ({mod:+d})"
    await ctx.send(f"🎲 {spec} -> **{total}**  [{detail}]")


@bot.command()
async def flip(ctx):
    """flip a coin"""
    await ctx.send(f"🪙 {random.choice(['heads', 'tails'])}")


@bot.command(name="8ball")
async def eight_ball(ctx, *, question: str = ""):
    """magic 8 ball"""
    if not question:
        await ctx.send("ask me a question: `!8ball will it rain?`")
        return
    await ctx.send(f"🎱 {random.choice(EIGHT_BALL)}")


@bot.command()
async def choose(ctx, *, options: str):
    """pick one. separate choices with | or commas"""
    parts = [p.strip() for p in re.split(r"[|,]", options) if p.strip()]
    if len(parts) < 2:
        await ctx.send("give me at least two choices: `!choose pizza | tacos`")
        return
    await ctx.send(f"i pick: **{random.choice(parts)}**")


@bot.command()
async def say(ctx, *, text: str):
    """echo text back and delete the original command"""
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass
    await ctx.send(text)


@bot.command()
async def avatar(ctx, member: discord.Member = None):
    """show a user's avatar"""
    member = member or ctx.author
    embed = discord.Embed(title=f"{member.display_name}'s avatar")
    embed.set_image(url=member.display_avatar.url)
    await ctx.send(embed=embed)


@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    """basic info about a user"""
    member = member or ctx.author
    embed = discord.Embed(title=str(member), color=member.color)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.add_field(name="id", value=member.id, inline=False)
    embed.add_field(
        name="joined", value=member.joined_at.strftime("%Y-%m-%d") if member.joined_at else "?"
    )
    embed.add_field(name="account made", value=member.created_at.strftime("%Y-%m-%d"))
    embed.add_field(name="roles", value=len(member.roles) - 1)
    await ctx.send(embed=embed)


@bot.command(name="help")
async def help_cmd(ctx):
    """list the commands"""
    lines = ["**commands:**"]
    for cmd in sorted(bot.commands, key=lambda c: c.name):
        lines.append(f"`{PREFIX}{cmd.name}` — {cmd.help or 'no description'}")
    await ctx.send("\n".join(lines))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"missing something. `{PREFIX}help` for usage.")
        return
    await ctx.send(f"oops: `{error}`")


def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise SystemExit(
            "no DISCORD_TOKEN found. copy .env.example to .env and put your token in it."
        )
    bot.run(token)


if __name__ == "__main__":
    main()
