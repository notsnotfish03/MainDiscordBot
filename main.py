import discord
import os
import random
import hidden
from discord import app_commands
from discord.ext import commands
from hero_enum import HeroEnum
from hero_enum import RoleEnum
from itertools import cycle
from discord.ext import tasks
from pretty_help import PrettyHelp




COIN_IMAGE_URL = "https://images.blz-contentstack.com/v3/assets/blt2477dcaf4ebd440c/blt07f15d602abb81a5/shop_icon?format=png&quality=90"

bot = commands.Bot(command_prefix='!', description='ooga booga dooga', intents=discord.Intents.all())

pretty_help = PrettyHelp(
    no_category="Overwatch",
    show_index=True
)

bot.help_command = pretty_help
status = cycle(['Overwatch 1', 'Overwatch 2'])

token = hidden.secret

@bot.event
async def on_ready():
  change_status.start()
  print("Your bot is ready")
  try:
    synced = await bot.tree.sync()
    print(f"synced {len(synced)} command(s)")
  except Exception as e:
    print(e)

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))


@bot.command(name='hero')
async def hero(ctx, *args):
    if args and args[0].lower() in ["tank", "dps", "support"]:
        match args[0]:
            case "tank":
                a_hero = HeroEnum.random_tank()
            case "dps":
                a_hero = HeroEnum.random_dps()
            case "support":
                a_hero = HeroEnum.random_support()
    else:
        a_hero = HeroEnum.random_hero()
    embed = discord.Embed(title="OW2 Hero Roulette", color=int(a_hero.role.color, 16))
    embed.set_thumbnail(url=a_hero.avatar_url)
    embed.add_field(name="Role", value=a_hero.role.value, inline=True)
    embed.add_field(name="Hero", value=a_hero.name.title(), inline=True)
    embed.set_footer(text="Powered by OW2 Hero Roulette", icon_url=COIN_IMAGE_URL)
    await ctx.send(embed=embed)

def generate_random_team(roles):
    team = []
    heroes_added = []

    for role in roles:
        if role == RoleEnum.TANK:
            hero = HeroEnum.random_tank()
        elif role == RoleEnum.DPS:
            hero = HeroEnum.random_dps()
        elif role == RoleEnum.SUPPORT:
            hero = HeroEnum.random_support()

        while hero in heroes_added:
            if role == RoleEnum.TANK:
                hero = HeroEnum.random_tank()
            elif role == RoleEnum.DPS:
                hero = HeroEnum.random_dps()
            elif role == RoleEnum.SUPPORT:
                hero = HeroEnum.random_support()

        heroes_added.append(hero)
        team.append(hero)

    return team



@bot.command(name="team")
async def generate_team(ctx):
    # Generate a team of heroes
    roles = [RoleEnum.TANK, RoleEnum.DPS, RoleEnum.DPS, RoleEnum.SUPPORT, RoleEnum.SUPPORT]
    team = generate_random_team(roles)

    # Create an embed for the team
    embed = discord.Embed(title="Your Totally Random Overwatch 2 Team")
    embed.set_thumbnail(url="https://cdn2.psychologytoday.com/assets/styles/manual_crop_1_91_1_1528x800/public/2020-08/shutterstock_1731284125_0.jpg")
    for role in RoleEnum:
        heroes = [hero.name.title() for hero in team if hero.role == role]
        if heroes:
            embed.add_field(name=f"{role.value}:", value=", ".join(heroes), inline=False)

    embed.set_footer(text="Powered uroboro's dungeon", icon_url="https://cdn-icons-png.flaticon.com/512/2014/2014307.png")
    await ctx.send(embed=embed)


    # Send team as a formatted string with "Your team is" prefix
    team_str = "Your team is:\n"
    for a_hero in team:
        team_str += f"{a_hero.name.title()} ({a_hero.role.value})\n"
    await ctx.send(team_str)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
	await interaction.response.send_message(f"{interaction.user.mention} you is a bitch") 
  
if __name__ == "__main__":
    bot.run(token)
