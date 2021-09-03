version = '0.0.3b'
import os, discord, json, time, aiohttp, datetime, string, io, asyncio, sys, ctypes, random, requests, urllib.parse, base64, pypresence
from colorama import Fore, Style, init
from discord.ext import commands
from discord.ext import tasks
from urllib.parse import urlencode
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4
from discord_webhook import DiscordWebhook
init(convert=True)

with open('config.json') as ok:
    config = json.load(ok)
    prefix = config.get("prefix")

try:
    config.get("prefix")
except:
    config.update({"prefix":"."})
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

spectraselfbot = commands.Bot(description='Spectra Selfbot.', command_prefix=prefix, self_bot=True)
spectraselfbot.remove_command('help')
rpc = pypresence.Presence(883344467724206110)
rpc.connect()
ctypes.windll.kernel32.SetConsoleTitleW(f'Loading...')
motdz = requests.get("https://raw.githubusercontent.com/Spectra-Selfbot/spectra/main/ext/motd.txt").text

def ready():
    os.system("mode 95,25")
    timeoflogin = datetime.datetime.now().strftime("%H:%M %p") 
    print(f'''{Fore.RESET} 
                                              {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|                            {Fore.BLUE}.-.{Fore.MAGENTA},="``"=.
      {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|  {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|      {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|      {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|  {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}|  {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}|  {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}|    {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}{Fore.MAGENTA}|    {Fore.BLUE}'={Fore.MAGENTA}/{Fore.BLUE}_       {Fore.MAGENTA}\\
    {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|      {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|    {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|  {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|  {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|          {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|      {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|      {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|    {Fore.BLUE}{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|     {Fore.MAGENTA}|{Fore.BLUE}  '=._    {Fore.MAGENTA}|
        {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|  {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|    {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|  {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|        {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|          {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|      {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|        {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|    {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|      {Fore.MAGENTA}\     {Fore.BLUE}`=.{Fore.MAGENTA}/{Fore.BLUE}`,
    {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|    {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|      {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|    {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|      {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|  {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|          {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|{Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|       {Fore.MAGENTA}'=.__.=' {Fore.BLUE}`=' 
              {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|
              {Fore.BLUE}{Fore.BLUE}_{Fore.MAGENTA}|
                                                                                                                                                    
{Fore.MAGENTA}C{Fore.BLUE}o{Fore.MAGENTA}n{Fore.BLUE}s{Fore.MAGENTA}o{Fore.BLUE}l{Fore.MAGENTA}e {Fore.BLUE}l{Fore.MAGENTA}o{Fore.BLUE}g{Fore.MAGENTA}s{Fore.BLUE}.{Fore.MAGENTA}.{Fore.BLUE}.
'''+Fore.RESET)    
    time.sleep(0.2)
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{timeoflogin}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}MOTD {Fore.MAGENTA}| {Fore.WHITE}{motdz}\n{Fore.MAGENTA}[{Fore.WHITE}{timeoflogin}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Logged In {Fore.MAGENTA}| {Fore.WHITE}Successfuly logged in to {Fore.MAGENTA}{spectraselfbot.user.name}{Fore.BLUE}#{Fore.MAGENTA}{spectraselfbot.user.discriminator}.\n{Fore.MAGENTA}[{Fore.WHITE}{timeoflogin}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Logged In {Fore.MAGENTA}| {Fore.WHITE}Prefix: {prefix}\n{Fore.MAGENTA}[{Fore.WHITE}{timeoflogin}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Logged In {Fore.MAGENTA}| {Fore.WHITE}Connected To {len(list(spectraselfbot.guilds))} server(s).\n{Fore.MAGENTA}[{Fore.WHITE}{timeoflogin}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Logged In {Fore.MAGENTA}| {Fore.WHITE}Connected To {len(list(spectraselfbot.user.friends))} friend(s).")

@spectraselfbot.event
async def on_message(message):
    if 'giveaway' in message.content:
        try:    
            await message.add_reaction("🎉")
        except discord.errors.Forbidden:
            time = datetime.datetime.now().strftime("%H:%M %p") 
            print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}x{Fore.MAGENTA}] {Fore.WHITE}Error {Fore.MAGENTA}| {Fore.WHITE}Failed to react to giveaway in {message.guild}."+Fore.RESET)
        timeofga = datetime.datetime.now().strftime("%H:%M %p")
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{    timeofga}{Fore.MAGENTA}] |{Fore.BLUE} Giveaway Entered {Fore.MAGENTA}| {Fore.WHITE}{message.guild} {Fore.MAGENTA}| {Fore.WHITE}#{message.channel}")

    if spectraselfbot.user.mentioned_in(message):
        timeofmetnion = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{timeofmetnion}{Fore.MAGENTA}] |{Fore.BLUE} {message.author} {Fore.WHITE}has mentioned you in {Fore.MAGENTA}| {Fore.WHITE}{message.guild} {Fore.MAGENTA}| {Fore.WHITE}#{message.channel}")
        try:
            now = datetime.datetime.now()
            with open('Logs\PingLogs.txt', 'a+') as f:
               f.write(f"[D{now.day}:H{now.hour}:M{now.minute}:S{now.second}] | {message.author} has mentioned you in | {message.guild} | #{message.channel}"+"\n" )
        except UnicodeEncodeError:
            pass
        
        if 'giveaway' in message.content:
            try:
                await message.add_reaction('🎉')
            except discord.errors.Forbidden:
                time534 = datetime.datetime.now().strftime("%H:%M %p") 
                print(f"{Fore.MAGENTA}[{Fore.WHITE}{time534}{Fore.MAGENTA}] [{Fore.BLUE}x{Fore.MAGENTA}] {Fore.WHITE}Error {Fore.MAGENTA}| {Fore.WHITE}Failed to add reaction to giveaway."+Fore.RESET)
                with open('Logs\ErrorLog.txt', 'a+') as f:
                    now = datetime.datetime.now()
                    f.write(f"[D{now.day}:H{now.hour}:M{now.minute}:S{now.second}]-[PERMISSION-ERROR] Failed to add reaction to giveaway."+"\n" )

    else:
        await spectraselfbot.process_commands(message)
        
#On connect goto ready
@spectraselfbot.event
async def on_connect():
    os.system("cls")
    print(f"{Fore.MAGENTA}[{Fore.BLUE}+{Fore.MAGENTA}]{Fore.WHITE} Redirecting...")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Spectra-Selfbot | Logged in as {spectraselfbot.user.name}#{spectraselfbot.user.discriminator}')
    ready()



@spectraselfbot.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.CheckFailure):
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}x{Fore.MAGENTA}] {Fore.WHITE}Error {Fore.MAGENTA}| {Fore.WHITE}Missing permission."+Fore.RESET)
        embed = discord.Embed(title="Error", color=0xffffff)
        embed.add_field(name=f"Missing permission", value=f"You're missing permission to execute this command.", inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30)
        now = datetime.datetime.now()
        with open('Logs\ErrorLog.txt', 'a+') as f:
           f.write(f"[D{now.day}:H{now.hour}:M{now.minute}:S{now.second}]-[MISSING PERMISSIONS] You're missing permission to execute this command."+"\n" )
    elif isinstance(error, commands.MissingRequiredArgument):
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}x{Fore.MAGENTA}] {Fore.WHITE}Error {Fore.MAGENTA}| {Fore.WHITE}Missing arguments."+Fore.RESET)
        embed = discord.Embed(title="Error", color=0xffffff)
        embed.add_field(name=f"Missing arguments", value=f"{error}", inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30)
        now = datetime.datetime.now()
        with open('Logs\ErrorLog.txt', 'a+') as f:
           f.write(f"[D{now.day}:H{now.hour}:M{now.minute}:S{now.second}]-[MISSING ARGUMENTS] {error}"+"\n" )
    elif isinstance(error, discord.errors.Forbidden):
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}x{Fore.MAGENTA}] {Fore.WHITE}Error {Fore.MAGENTA}| {Fore.WHITE}{error}"+Fore.RESET)
        embed = discord.Embed(title="Error", color=0xffffff)
        embed.add_field(name=f"Discord error", value=f"{error}", inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30)
        now = datetime.datetime.now()
        with open('Logs\ErrorLog.txt', 'a+') as f:
           f.write(f"[D{now.day}:H{now.hour}:M{now.minute}:S{now.second}]-[DISCORD ERROR] {error}"+"\n" )
    elif "Cannot send an empty message" in error_str:
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}x{Fore.MAGENTA}] {Fore.WHITE}Error {Fore.MAGENTA}| {Fore.WHITE}Could not send an empty message."+Fore.RESET) 
        embed = discord.Embed(title="Error", color=0xffffff)
        embed.add_field(name=f"Failed to send message", value=f"Couldnt send a empty message.", inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30)     
        now = datetime.datetime.now()
        with open('Logs\ErrorLog.txt', 'a+') as f:
           f.write(f"[D{now.day}:H{now.hour}:M{now.minute}:S{now.second}]-[DISCORD ERROR] Cannot send an empty message."+"\n" )       
    else:
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}x{Fore.MAGENTA}] {Fore.WHITE}Error {Fore.MAGENTA}| {Fore.WHITE}{error_str}"+Fore.RESET)
        embed = discord.Embed(title="Error", color=0xffffff)
        embed.add_field(name=f"Other error", value=f"{error_str}", inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 
        now = datetime.datetime.now()
        with open('Logs\ErrorLog.txt', 'a+') as f:
           f.write(f"[D{now.day}:H{now.hour}:M{now.minute}:S{now.second}]-[OTHER ERROR] {error_str}"+"\n" ) 

@spectraselfbot.command(aliases=['frbu','backupfriends'])
async def friendbackup(ctx):
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} friendbackup")
    embed = discord.Embed(title="Friendbackup", color=0xffffff)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30) 
    for user in spectraselfbot.user.friends:
        try:
            with open('Backups\Friends.txt', 'a+') as f: 
                f.write(f"{user.name}#{user.discriminator}"+"\n")
        except:
            pass

@spectraselfbot.command()
async def help(ctx, help = None):
    await ctx.message.delete()
    if help is None:
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} help")
        embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁",  color=0xffffff)
        embed.add_field(name=f"{prefix}help text :speech_balloon:", value=f"```Our text commands.``` ", inline=True)
        embed.add_field(name=f"{prefix}help image :frame_photo:", value=f"```Our image commands. ```", inline=True)
        embed.add_field(name=f"{prefix}help nsfw :underage:", value=f"```Our nsfw commands.```", inline=True)
        embed.add_field(name=f"{prefix}help tools :tools:", value=f"```Our tool commands.```", inline=True)
        embed.add_field(name=f"{prefix}help trolling :skull:", value=f"```Our trolling commands.```", inline=True)
        embed.add_field(name=f"{prefix}help nuking :bomb:", value=f"```Our server nuke commands.```", inline=True)
        embed.add_field(name=f"{prefix}help fun :space_invader: ", value=f"```Our fun commands.```", inline=True)
        embed.add_field(name=f"{prefix}help misc :hotsprings:", value=f"```Our miscellaneous commands.``` ", inline=True)
        embed.add_field(name=f"{prefix}help animation :monkey: ", value=f"```Our animated commands.``` ", inline=True)
        embed.add_field(name=f"{prefix}help info :information_source:", value=f"```Our information commands.```", inline=True)
        embed.add_field(name=f"{prefix}help moderation :hammer_pick:", value=f"```Our moderation commands.```", inline=True)
        embed.add_field(name=f"{prefix}help other :fast_forward:", value=f"```Our other commands.``` ", inline=True)
        embed.set_image(url="https://media.discordapp.net/attachments/844294915596746812/862229059392372736/spectra_logo.png?width=891&height=200")
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 
    elif help == 'text':
        embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 text commands", description="> `<> Is Necessary, [] Is Optional.`", color=0xffffff)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/844294915596746812/862229059392372736/spectra_logo.png?width=891&height=200")
        embed.add_field(name=f"{prefix}emojitext (text)", value=f"```Turns text into ascii art.``` ", inline=True)
        embed.add_field(name=f"{prefix}emojitext (text)", value=f"```Turns text into ascii art.``` ", inline=True)
        embed.add_field(name=f"{prefix}ascii (text)", value=f"```Turns text into ascii art.``` ", inline=True)
        embed.add_field(name=f"{prefix}shrug", value=f"```¯\_(ツ)_/¯```", inline=True)
        embed.add_field(name=f"{prefix}lenny", value=f"```( ͡° ͜ʖ ͡°)```", inline=True)
        embed.add_field(name=f"{prefix}tableflip ", value=f"```(╯°□°）╯︵ ┻━┻```", inline=True)
        embed.add_field(name=f"{prefix}spoiler (text)", value=f"```Turns text into a spoiler.```", inline=True)
        embed.add_field(name=f"{prefix}bold (text) ", value=f"```Turns text bold.``` ", inline=True)
        embed.add_field(name=f"{prefix}italic (text)", value=f"```Turns text into italics.``` ", inline=True)
        embed.add_field(name=f"{prefix}underline (text)", value=f"```Underlines given text.``` ", inline=True)
        embed.add_field(name=f"{prefix}quote (text) ", value=f"```Turns text into a quote.``` ", inline=True)
        embed.add_field(name=f"{prefix}strike (text)", value=f"```Puts a strike through the text.``` ", inline=True)
        embed.add_field(name=f"{prefix}tos", value=f"```Sends 𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 TOS.```", inline=True)
        embed.add_field(name=f"{prefix}discordrules", value=f"```sends out discord server rules.``` ", inline=True)
        embed.add_field(name=f"{prefix}howgay (user)", value=f"```Finds out how gay the mentioned user is.``` ", inline=True)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 
    elif help == 'image':
        embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 image commands", description="> `<> Is Necessary, [] Is Optional.`", color=0xffffff)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/844294915596746812/862229059392372736/spectra_logo.png?width=891&height=200")
        embed.add_field(name=f"{prefix}hitler", value=f"```Sends an image of Adolf Hitler.``` ", inline=True)
        embed.add_field(name=f"{prefix}dog", value=f"```Sends random dog image.```", inline=False)
        embed.add_field(name=f"{prefix}cat", value=f"```Sends random cat image.```", inline=False)
        embed.add_field(name=f"{prefix}fox", value=f"```Sends random fox image.```", inline=False)
        embed.add_field(name=f"{prefix}panda", value=f"```Sends random panda image.```", inline=False)
        embed.add_field(name=f"{prefix}redpanda", value=f"```Sends random red panda image.```", inline=False)
        embed.add_field(name=f"{prefix}koala", value=f"```Sends random koala image.```", inline=False)
        embed.add_field(name=f"{prefix}bird", value=f"```Sends random bird image.```", inline=False)
        embed.add_field(name=f"{prefix}deepfry [user]", value=f"```Deepfrys users avatar.``` ", inline=True)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 
    elif help == 'nsfw':
        embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 nsfw commands", description="> `<> Is Necessary, [] Is Optional.`", color=0xffffff)
        embed.add_field(name=f"{prefix}hentai", value=f"```Sends random hentai gif.```", inline=False)
        embed.add_field(name=f"{prefix}boobs", value=f"```Sends random image of boobs.```", inline=False)
        embed.add_field(name=f"{prefix}lewdneko", value=f"```Random lewdneko gif.```", inline=False)
        embed.add_field(name=f"{prefix}lesbian", value=f"```Random lesbian image.```", inline=False)
        embed.add_field(name=f"{prefix}feed <user>", value=f"```Sends image/gif of you feeding mentioned user.```", inline=False)
        embed.add_field(name=f"{prefix}tickle <user>", value=f"```Sends image/gif of you tickling mentioned user.```", inline=False)
        embed.add_field(name=f"{prefix}slap <user>", value=f"```Sends image/gif of you slaping mentioned user.```", inline=False)
        embed.add_field(name=f"{prefix}hug <user>", value=f"```Sends image/gif of you hugging mentioned user.```", inline=False)
        embed.add_field(name=f"{prefix}smug <user>", value=f"```Sends smug version of mentioned user.```", inline=False)
        embed.add_field(name=f"{prefix}pat <user>", value=f"```Sends image/gif of you patting mentioned user.```", inline=False)
        embed.add_field(name=f"{prefix}kiss <user>", value=f"```Sends image/gif of you kissing mentioned user.```", inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 
    elif help == 'tools':
        embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 tool commands", description="> `<> Is Necessary, [] Is Optional.`", color=0xffffff)
        embed.add_field(name=f"{prefix}genpass <length>", value=f"```generates a secure password of the length specified.``` ", inline=True)
        embed.add_field(name=f"{prefix}delwebhook <webhook>", value=f"```deletes entered discord webhook.``` ", inline=True)
        embed.add_field(name=f"{prefix}sendwebhook <webhook> <message>", value=f"```sends message to entered discord webhook.``` ", inline=True)
        embed.add_field(name=f"{prefix}firstmsg", value=f"```sends first message in used channel/dm.``` ", inline=True)
        embed.add_field(name=f"{prefix}ip <ip address>", value=f"```looks up information on given ip address.``` ", inline=True)
        embed.add_field(name=f"{prefix}purge <amount>", value=f"```Deletes amount of messages in used channel.``` ", inline=True)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 
    elif help == 'trolling':
        embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 trolling commands", description="> `<> Is Necessary, [] Is Optional.`", color=0xffffff)
        embed.add_field(name=f"{prefix}massreact <emoji>", value=f"```Reacts specified emoji to above messages.``` ", inline=True)
        embed.add_field(name=f"{prefix}crashgif", value=f"```Sends a gif to crash the watchers discord.``` ", inline=True)
        embed.add_field(name=f"{prefix}hack [user]", value=f"```Joke hacks mentioned user.``` ", inline=True)
        embed.add_field(name=f"{prefix}mock <text>", value=f"```SpOnGe BoB MoCkS SoMeOnE lIkE tHiS.``` ", inline=True)
        embed.add_field(name=f"{prefix}spam <amount> <text>", value=f"```Spams text amount of times.``` ", inline=True)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 
    elif help == 'misc':
        embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 miscellaneous commands", description="> `<> Is Necessary, [] Is Optional.`", color=0xffffff)
        embed.add_field(name=f"{prefix}google <search>", value=f"```Sends a google search for entered search.``` ", inline=True)
        embed.add_field(name=f"{prefix}youtube <search>", value=f"```Sends a youtube search for entered search.``` ", inline=True)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    elif help == 'nuking':
        embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 nuking commands", description="> `<> Is Necessary, [] Is Optional.`", color=0xffffff)
        embed.add_field(name=f"coming soon", value=f"be patient bitch", inline=True)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    elif help == 'fun':
        embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 fun commands", description="> `<> Is Necessary, [] Is Optional.`", color=0xffffff)
        embed.add_field(name=f"{prefix}howgay [user]", value=f"```Uses magic abilites to find out how gay the mentioned user is.````", inline=True)
        embed.add_field(name=f"{prefix}8ball [question]", value=f"```Uses magic 8ball powers to figure out the answer to your question.````", inline=True)
        embed.add_field(name=f"{prefix}diceroll [question]", value=f"```Pretty simple, rolls a dice and shows you the answer.````", inline=True)
        embed.add_field(name=f"{prefix}rick [question]", value=f"```Guess you will have to find out your self...````", inline=True)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    elif help == 'animation':
        embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 animation commands", description="> `<> Is Necessary, [] Is Optional.`", color=0xffffff)
        embed.add_field(name=f"{prefix}cum", value=f"```You will have to try it out and see...````", inline=True)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)  
    elif help == 'info':
        embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 info commands", description="> `<> Is Necessary, [] Is Optional.`", color=0xffffff)
        embed.add_field(name=f"{prefix}serverinfo", value=f"```Gives you some information of used-in server.````", inline=True)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)  

@spectraselfbot.command(name='first-message', aliases=['firstmsg'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} firstmsg"+Fore.RESET)
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(title="First Message in this channel!", color=000000)
    embed.add_field(name="Press the hyper-link below to jump to the first message in used channel.", value=f"[Jump to message]({first_message.jump_url})")
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)    

@spectraselfbot.command()
async def hentai(ctx): 
    embed = discord.Embed(title="Hentai", description="Random hentai gif.", color=0xffffff)
    embed.set_image(url=str(requests.get("https://nekos.life/api/v2/img/Random_hentai_gif").json()["url"]))
    embed.set_footer(text=f"Requested by {ctx.message.author}.", icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)

@spectraselfbot.command()
async def boobs(ctx):
    embed = discord.Embed(title="Boobs", description="Random image of boobs.", color=0xffffff)
    embed.set_image(url=str(requests.get("https://nekos.life/api/v2/img/boobs").json()["url"]))
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)     

@spectraselfbot.command()
async def lewdneko(ctx):
    embed = discord.Embed(title="Lewdneko", description="Random lewdneko gif.", color=0xffffff)
    embed.set_image(url=str(requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif").json()["url"]))
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)     

@spectraselfbot.command()
async def lesbian(ctx):
    embed = discord.Embed(title="Lesbian", description="Random lesbian image.", color=0xffffff)
    embed.set_image(url=str(requests.get("https://nekos.life/api/v2/img/les").json()["url"]))
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)     

@spectraselfbot.command()  
async def feed(ctx, user: discord.User):
    embed = discord.Embed(title="feed", description=f"You fed <@{user.id}>.", color=0xffffff)
    embed.set_image(url=str(requests.get("https://nekos.life/api/v2/img/feed").json()["url"]))
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)   

@spectraselfbot.command()
async def tickle(ctx, user: discord.User = None):
    embed = discord.Embed(title="tickle", description=f"You tickled <@{user.id}>.", color=0xffffff)
    embed.set_image(url=str(requests.get("https://nekos.life/api/v2/img/tickle").json()["url"]))
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)   

@spectraselfbot.command()
async def slap(ctx, user: discord.User = None):
    embed = discord.Embed(title="slap", description=f"You slapped <@{user.id}>.", color=0xffffff)
    embed.set_image(url=str(requests.get("https://nekos.life/api/v2/img/slap").json()["url"]))
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)   

@spectraselfbot.command()
async def hug(ctx, user: discord.User = None):
    embed = discord.Embed(title="hug", description=f"You hugged <@{user.id}>.", color=0xffffff)
    embed.set_image(url=str(requests.get("https://nekos.life/api/v2/img/hug").json()["url"]))
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)   

@spectraselfbot.command()
async def smug(ctx, user: discord.User = None):
    embed = discord.Embed(title="smug", description=f"smug <@{user.id}>.", color=0xffffff)
    embed.set_image(url=str(requests.get("https://nekos.life/api/v2/img/smug").json()["url"]))
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)   

@spectraselfbot.command()
async def pat(ctx, user: discord.User = None):
    embed = discord.Embed(title="pat", description=f"You pat <@{user.id}>.", color=0xffffff)
    embed.set_image(url=str(requests.get("https://nekos.life/api/v2/img/pat").json()["url"]))
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)   

@spectraselfbot.command()
async def kiss(ctx, user: discord.User):
    embed = discord.Embed(title="kiss", description=f"You kissed <@{user.id}>.", color=0xffffff)
    embed.set_image(url=str(requests.get("https://nekos.life/api/v2/img/kiss").json()["url"]))
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@spectraselfbot.command()
async def dog(ctx):
    ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} dog"+Fore.RESET)
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    embed = discord.Embed()
    embed = discord.Embed(title="Dog", description="Random dog image.", color=0xffffff)
    embed.set_image(url=str(r['message']))
    embed.set_footer(text=f"𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed,  delete_after=30)

@spectraselfbot.command()
async def fox(ctx): 
    ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} fox"+Fore.RESET)
    r = requests.get("https://randomfox.ca/floof/").json()
    embed = discord.Embed()
    embed = discord.Embed(title="Fox", description="Random fox image.", color=0xffffff)
    embed.set_image(url=str(r['image']))
    embed.set_footer(text=f"𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed,  delete_after=30)

@spectraselfbot.command()
async def cat(ctx): 
    ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} cat"+Fore.RESET)
    r = requests.get("https://api.thecatapi.com/v1/images/search?format=json&x-api-key=").json()
    embed = discord.Embed()
    embed = discord.Embed(title="Cat", description="Random cat image.", color=0xffffff)
    embed.set_image(url=str(r[0]["url"]))
    embed.set_footer(text=f"𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed,  delete_after=30)

@spectraselfbot.command()
async def panda(ctx): 
    ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} panda"+Fore.RESET)
    r = requests.get("https://some-random-api.ml/img/panda").json()
    embed = discord.Embed()
    embed = discord.Embed(title="Panda", description="Random panda image.", color=0xffffff)
    embed.set_image(url=str(r["link"]))
    embed.set_footer(text=f"𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed,  delete_after=30)

@spectraselfbot.command()
async def redpanda(ctx): 
    ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} redpanda"+Fore.RESET)
    r = requests.get("https://some-random-api.ml/img/red_panda").json()
    embed = discord.Embed()
    embed = discord.Embed(title="RedPanda", description="Random red panda image.", color=0xffffff)
    embed.set_image(url=str(r["link"]))
    embed.set_footer(text=f"𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed,  delete_after=30)


@spectraselfbot.command()
async def koala(ctx): 
    ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} koala"+Fore.RESET)
    r = requests.get("https://some-random-api.ml/img/koala").json()
    embed = discord.Embed()
    embed = discord.Embed(title="Koala", description="Random koala image.", color=0xffffff)
    embed.set_image(url=str(r["link"]))
    embed.set_footer(text=f"𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed,  delete_after=30)

@spectraselfbot.command()
async def bird(ctx): 
    ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} dog"+Fore.RESET)
    r = requests.get("https://some-random-api.ml/img/birb").json()
    embed = discord.Embed()
    embed = discord.Embed(title="Bird", description="Random bird image.", color=0xffffff)
    embed.set_image(url=str(r["link"]))
    embed.set_footer(text=f"𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed,  delete_after=30)

@spectraselfbot.command()
async def sendwebhook(ctx, webhook, *, message):
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} sendwebhook"+Fore.RESET)
    embed = discord.Embed(title="sendwebhook", color=000000)
    embed.add_field(name=f"Webhook", value=webhook, inline=False)
    embed.add_field(name=f"Content", value=message, inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30) 
    webhook1 = DiscordWebhook(url=webhook, content=message)
    response = webhook1.execute()

@spectraselfbot.command()
async def howgay(ctx, *, user: discord.User = None):
    await ctx.message.delete()     
    if user is None:
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} howgay"+Fore.RESET)
        embed = discord.Embed(title=f"`{ctx.message.author}` is {random.randint(0,100)}% Gay!  :rainbow_flag:", color=0xffffff)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30)    
    elif user.id == 852580967201898517:
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} howgay"+Fore.RESET)
        embed = discord.Embed(title=f"`{ctx.message.author}` is 100% Gay!  :rainbow_flag:", color=0xffffff)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30)  
    else:
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} howgay"+Fore.RESET)
        embed = discord.Embed(title=f"`{ctx.message.author}` is {random.randint(0,100)}% Gay!  :rainbow_flag:", color=0xffffff)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 

@spectraselfbot.command()
async def lookup(ctx, ip):
    lookup = ("http://ip-api.com/json/" + ip + "?fields=status,message,country,countryCode,region,regionName,city,zip,isp,as,query")
    with urllib.request.urlopen(lookup) as url:
        data = json.loads(url.read().decode())       
    sts = ip
    if sts == "?":
       embed = discord.Embed(title=f"Failed to lookup {ip}.", color=0xffffff)
       embed.set_footer(text=f"Requested by {ctx.message.author}.", icon_url=ctx.author.avatar_url)
       await ctx.reply(embed=embed)
    if sts == "/":
       embed = discord.Embed(title=f"Failed to lookup {ip}.", color=0xffffff)
       embed.set_footer(text=f"Requested by {ctx.message.author}.", icon_url=ctx.author.avatar_url)
       await ctx.reply(embed=embed)
    if data["query"] == "90.246.49.117":
       embed = discord.Embed(title=f"Failed to lookup {ip}.", color=0xffffff)
       embed.set_footer(text=f"Requested by {ctx.message.author}.", icon_url=ctx.author.avatar_url)
       await ctx.reply(embed=embed)
    else:
        country = data["country"]
        region = data["regionName"]
        city = data["city"]
        zip = data["zip"]
        isp = data["isp"]
        ipname = data["as"]
        status = data["status"]

        embed = discord.Embed(title=f"Lookup {ip}", color=0xffffff)
        embed.add_field(name="County:", value=f"`{country}`", inline=False)
        embed.add_field(name="Region:", value=f"`{region}`", inline=False)
        embed.add_field(name="City:", value=f"`{city}`", inline=False)
        embed.add_field(name="Zip:", value=f"`{zip}`", inline=False)
        embed.add_field(name="Isp:", value=f"`{isp}`", inline=False)
        embed.add_field(name="IpName:", value=f"`{ipname}`", inline=False)
        embed.add_field(name="Status:", value=f"`{status}`", inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30)

@spectraselfbot.command(name='8ball') 
async def _ball(ctx, *, question): 
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} 8ball"+Fore.RESET) 
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(title="Magic 8 Ball...", color=0xffffff)
    embed.add_field(name="question:", value=f"{question}", inline=False)
    embed.add_field(name="answer:", value=f"{answer}", inline=False)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/841066587545141278/848285446885998652/8ball.png?width=676&height=676")
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)
    
@spectraselfbot.command()
async def halftoken(ctx, user: discord.User = None):
    await ctx.message.delete()
    base64_bytes = user.id.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    embed = discord.Embed(title="halftoken", color=0xffffff)
    embed.add_field(name=f"Half of {user}'s token is", value=f"{sample_string}", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)

@spectraselfbot.command()  
async def lock(ctx): 
    await ctx.message.delete()
    ctypes.windll.user32.LockWorkStation()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} lock"+Fore.RESET) 
    embed = discord.Embed(title="Lock", description="Successfully locked workstation.",color=0xffffff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/841066587545141278/848285903805612036/lock.png?width=676&height=676")
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)

@spectraselfbot.command()  
async def cls(ctx): 
    await ctx.message.delete()
    embed = discord.Embed(title="cls", description="Cleared Console",color=0xffffff)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)
    os.system("cls")
    ready()

@spectraselfbot.command() 
async def credits(ctx): 
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} credits"+Fore.RESET) 
    embed = discord.Embed(title="Credits", color=0xffffff)
    embed.add_field(name="Discord:", value=f"`</Octo>#0001`", inline=False)
    embed.add_field(name="Discord Server:", value=f"[Our discord server](https://discord.gg/octo)", inline=False)
    embed.add_field(name="Github:", value=f"[My github profile](https://github.com/Oct0-xox \"my github profile!\")", inline=False)
    embed.add_field(name="Youtube:", value=f"[My youtube profile](https://www.youtube.com/channel/UCghxsJx-Afv9LfB1L-lOH9A \"my youtube channel <3\")", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)
    
@spectraselfbot.command() 
async def Crashgif(ctx): 
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} crashgif"+Fore.RESET) 
    await ctx.send('https://giant.gfycat.com/ThoseVastHyena.mp4')
    
    
@spectraselfbot.command() 
async def crashgif(ctx): 
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} crashgif"+Fore.RESET) 
    await ctx.send('https://giant.gfycat.com/ThoseVastHyena.mp4')

@spectraselfbot.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} 911"+Fore.RESET) 
    invis = ""  
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')
        
@spectraselfbot.command(aliases=["servinfo"])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"serverinfo", color=0xffffff)
    embed.add_field(name="Guild Name", value=f"`{ctx.guild.name}`", inline=False)
    embed.add_field(name="Members", value=f"`{len(ctx.guild.members)}`", inline=False)
    embed.add_field(name="Roles", value=f"`{len(ctx.guild.roles)}`", inline=False)
    embed.add_field(name="Text Channels", value=f"`{len(ctx.guild.text_channels)}`", inline=False)
    embed.add_field(name="Voice Channels", value=f"`{len(ctx.guild.voice_channels)}`", inline=False)
    embed.add_field(name="Categories", value=f"`{len(ctx.guild.categories)}`")
    embed.add_field(name="Server created at", value=f"`{ctx.guild.created_at.strftime(date_format)}`", inline=False)
    embed.add_field(name="Server Owner", value=f"`{ctx.guild.owner}`", inline=False)
    embed.add_field(name="Server Region", value=f"`{ctx.guild.region}`", inline=False)
    embed.add_field(name="Server ID", value=f"`{ctx.guild.id}`", inline=False)
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)

    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} serverinfo"+Fore.RESET) 

@spectraselfbot.command()
async def av(ctx, *, user: discord.User = None):
    if user is None:
        user = ctx.message.author
    embed = discord.Embed(title="Av", description=f"{user}'s Avatar.", color=0xffffff)
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)

@spectraselfbot.command(aliases=["jerkoff", "ejaculate", "orgasm", "wank", "jerk"])
async def cum(ctx):
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} cum"+Fore.RESET) 
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.1)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.1)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.1)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.1)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.1)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.1)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.1)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.1)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
     
@spectraselfbot.command() 
async def spam(ctx, amount: int, *, message): 
    await ctx.message.delete()    
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} spam"+Fore.RESET) 
    for _i in range(amount):
        await ctx.send(message)

        
@spectraselfbot.command() 
async def ascii(ctx, *, text): 
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} ascii"+Fore.RESET) 
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@spectraselfbot.command() 
async def google(ctx, *, search): 
    await ctx.message.delete()
    text = search.replace(' ', '+')
    embed = discord.Embed(title="Google", color=0xffffff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/865947376249208852/865949296460955648/818ff7a3edc40836182c585939fbe82a.png")
    embed.add_field(name=f"Google search for {search}", value=f"[Press here for search results](https://www.google.com/search?q={text} \"Search results for {search}\")", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} google"+Fore.RESET)    
    
@spectraselfbot.command() 
async def youtube(ctx, *, search): 
    await ctx.message.delete()
    text = search.replace(' ', '+')
    embed = discord.Embed(title="Youtube Search", color=0xffffff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/866714557857792000/867284669933682708/youtube.png?width=523&height=522")
    embed.add_field(name=f"Youtube search for {search}", value=f"[Press here for youtube search results](https://www.youtube.com/results?search_query={text} \"Youtube search results for {search}\")", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} youtube"+Fore.RESET)    

@spectraselfbot.command() 
async def shutdown(ctx): 
    await ctx.message.delete()
    embed = discord.Embed(title="Shutdown", description="See you next time!", color=0xffffff)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)
    os.system("shutdown /s /t 1")

@spectraselfbot.command() 
async def stream(ctx, url , *, message): 
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} stream"+Fore.RESET) 
    embed = discord.Embed(title="Stream", color=0xffffff)
    embed.add_field(name=f"Set Stream Title To {message}", value=f"Make sure to set your stream link in the config.json file!", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30) 
    stream = discord.Streaming(name=message, url=url)
    await spectraselfbot.change_presence(activity=stream) 
    
    
@spectraselfbot.command() 
async def shrug(ctx): 
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} shrug"+Fore.RESET) 

@spectraselfbot.command() 
async def lenny(ctx): 
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} lenny"+Fore.RESET) 

@spectraselfbot.command() 
async def tableflip(ctx): 
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} tableflip"+Fore.RESET) 

@spectraselfbot.command() 
async def unflip(ctx): 
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} unflip"+Fore.RESET)

@spectraselfbot.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


@spectraselfbot.command()
async def censor(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')


@spectraselfbot.command()
async def underline(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('__' + message + '__')


@spectraselfbot.command()
async def italic(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')


@spectraselfbot.command()
async def strike(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('~~' + message + '~~')


@spectraselfbot.command()
async def quote(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('> ' + message)


@spectraselfbot.command() 
async def uptime(ctx): 
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow()
    uptime = str(uptime).split('.')[0]
    embed = discord.Embed(title="uptime", color=0xffffff)
    embed.add_field(name="Uptime:", value=f"{uptime}", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} uptime"+Fore.RESET)

@spectraselfbot.command() 
async def ping(ctx): 
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} ping"+Fore.RESET)
    embed = discord.Embed(title="ping", color=0xffffff)
    embed.add_field(name=f"Your Ping Is:", value=f"{round(spectraselfbot.latency *1000)}ms.", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)

@spectraselfbot.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): 
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        embed = discord.Embed(title="hypesquad", color=0xffffff)
        embed.add_field(name=f"Set Hypesquad To:", value=f"{house}", inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30)
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} hypesquad"+Fore.RESET)
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        pass

@spectraselfbot.command() 
async def quit(ctx): 
    await ctx.message.delete()
    sys.exit() 

@spectraselfbot.command(name='1337speak', aliases=['leetspeak'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'{text}')
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} 1337speak"+Fore.RESET)

@spectraselfbot.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR').json()
    usd = r['USD']
    eur = r['EUR']
    embed = discord.Embed(title="bitcoin", description="Current BTC Price.", color=0xffffff)
    embed.set_thumbnail(url="https://pngimg.com/uploads/bitcoin/bitcoin_PNG48.png")
    embed.add_field(name=f"USD", value=f"`{str(usd)}$`", inline=False)
    embed.add_field(name=f"EUR", value=f"`{str(eur)}€`", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} bitcoin"+Fore.RESET)

@spectraselfbot.command(aliases=["gcleave"])
async def leavegc(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="leavegc", color=0xffffff)
    embed.add_field(name="Left Groupchat", value=f"Good bye!", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()
        time = datetime.datetime.now().strftime("%H:%M %p")
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} leavegc"+Fore.RESET)

@spectraselfbot.command() 
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} massreact"+Fore.RESET)

@spectraselfbot.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups', "groupleave", "groupleaver"])
async def _group_leaver(ctx):
    await ctx.message.delete()
    for channel in spectraselfbot.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()
            embed = discord.Embed(title="leaveallgroups", description="Good bye groupchats.", color=0xffffff)
            embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed, delete_after=30)
            time = datetime.datetime.now().strftime("%H:%M %p") 
            print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} leaveallgroups"+Fore.RESET) 

@spectraselfbot.command() 
async def version(ctx): 
    await ctx.message.delete()
    embed = discord.Embed(title=f"You are on 𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 version `{version}`", color=0xffffff)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} version"+Fore.RESET)


@spectraselfbot.command() 
async def diceroll(ctx): 
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} diceroll"+Fore.RESET)
    filenameforgif = 'dice_rolling.gif'
    embedgif = discord.Embed(title="diceroll", description="Rolling dice...", color=0xffffff)
    embedgif.set_image(url="https://media.discordapp.net/attachments/843150293440135189/855450084703076422/dice_rolling.gif")
    embedgif.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁")
    await ctx.send(embed=embedgif, delete_after=3)
    await asyncio.sleep(3)
    responses = [
      "https://media.discordapp.net/attachments/843150293440135189/855450086096109568/Dice_1.png",
"https://media.discordapp.net/attachments/843150293440135189/855450088020639754/Dice_2.png",
"https://media.discordapp.net/attachments/843150293440135189/855450089392963604/Dice_3.png",
"https://media.discordapp.net/attachments/843150293440135189/855450090738548766/Dice_4.png",
"https://media.discordapp.net/attachments/843150293440135189/855450092529385492/Dice_5.png",
"https://media.discordapp.net/attachments/843150293440135189/855450083235332156/Dice_6.png",
    ]
    filename = random.choice(responses)
    embed = discord.Embed(title="diceroll", color=0xffffff)
    embed.add_field(name="Done Rolling dice!", value=f"ur hot", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    embed.set_image(url=filename)
    await ctx.send(embed=embed, delete_after=30)

@spectraselfbot.command() 
async def notfunny(ctx): 
    await ctx.message.delete()
    await ctx.send(f"Not funny I didn't laugh. Your joke is so bad I would have preferred the joke went over my head and you gave up re-telling me the joke. To be honest this is a horrid attempt at trying to get a laugh out of me. Not a chuckle, not a hehe, not even a subtle burst of air out of my esophagus. Science says before you laugh your brain preps your face muscles but I didn't even feel the slightest twitch. 0/10 this joke is so bad I cannot believe anyone legally allowed you to be creative at all. The amount of brain power you must have put into that joke has the potential to power every house on Earth. Get a personality and learn how to make jokes, read a book. I'm not saying this to be funny I genuinely mean it on how this is just bottom barrel embarrassment at comedy. You've single handedly killed humor and every comedic act on the planet. I'm so disappointed that society has failed as a whole in being able to teach you how to be funny. Honestly if I put in all my power and time to try and make your joke funny it would require Einstein himself to build a device to strap me into so I can be connected to the energy of a billion stars to do it, and even then all that joke would get from people is a subtle scuff. You're lucky I still have the slightest of empathy for you after telling that joke otherwise I would have committed every war crime in the book just to prevent you from attempting any humor ever again. We should put that joke in text books so future generations can be wary of becoming such an absolute comedic failure. Im disappointed, hurt, and outright offended that my precious time has been wasted in my brain understanding that joke. In the time that took I was planning on helping kids who have been orphaned, but because of that you've waisted my time explaining the obscene integrity of your terrible attempt at comedy. Now those kids are suffering without")   
    await ctx.send(f"meals and there's nobody to blame but you. I hope you're happy with what you have done and I truly hope you can move on and learn from this piss poor attempt.")   
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} notfunny"+Fore.RESET)
    
@spectraselfbot.command()
async def rick(ctx):
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} rick"+Fore.RESET) 
    message = await ctx.send('''We're no strangers to love''')
    await asyncio.sleep(2)
    await message.edit(content='''You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy''')
    await asyncio.sleep(2)
    await message.edit(content='''I just wanna tell you how I'm feeling
Gotta make you understand''')
    await asyncio.sleep(2)
    await message.edit(content='''Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you''')
    await asyncio.sleep(4)
    await message.edit(content='''We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it''')
    await asyncio.sleep(4)
    await message.edit(content='''And if you ask me how I'm feeling
Don't tell me you're too blind to see''')
    await asyncio.sleep(2)
    await message.edit(content='''Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you''')
    await asyncio.sleep(4)
    await message.edit(content='''Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you''')
    await asyncio.sleep(4)
    await message.edit(content='''(Ooh, give you up)
(Ooh, give you up)
Never gonna give, never gonna give
(Give you up)
Never gonna give, never gonna give
(Give you up)''')
    await asyncio.sleep(4)
    await message.edit(content='''We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it
''')
    await asyncio.sleep(4)
    await message.edit(content='''I just wanna tell you how I'm feeling
Gotta make you understand
''')
    await asyncio.sleep(2)
    await message.edit(content='''Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
''')
    await asyncio.sleep(4)
    await message.edit(content='''Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you''')
    await asyncio.sleep(4)
    await message.edit(content='''Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
''')
    await asyncio.sleep(4)
    await message.edit(content='''hehe''')

@spectraselfbot.command(name='clp', aliases=['clap'])
async def clapz(ctx, *, text):
    await ctx.message.delete()
    text = text.replace(' ', ':clap_tone4:')
    await ctx.send(f'{text}')
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} clap"+Fore.RESET)

@spectraselfbot.command()
async def mock(ctx, *, message):
    await ctx.message.delete()
    out = ''.join(random.choice((str.upper, str.lower))(c) for c in message)
    await ctx.send(out)
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} mock"+Fore.RESET)

@spectraselfbot.command()
async def gping(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(f'{message}', delete_after=1)
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} gping"+Fore.RESET)

@spectraselfbot.command()
async def purge(ctx, amount: int): 
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} purge"+Fore.RESET)
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == spectraselfbot.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass
            embed = discord.Embed(title="purge", color=0xffffff)
            embed.add_field(name=f"Purging {amount} messages...", value=f"⠀", inline=False)
            embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed, delete_after=30)

@spectraselfbot.command(aliases=["deepfry"])
async def fry(ctx, user: discord.User = None):
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} deepfry"+Fore.RESET)
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"spectraselfbot_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"spectraselfbot_fry.png"))
        except:
            await ctx.send(res['message'])

@spectraselfbot.command()
async def wouldyourather(ctx):
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} wouldyourather"+Fore.RESET)
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    embed = discord.Embed(title="Would You Rather", color=0xffffff)
    embed.add_field(name="🅰", value=f"{qa}", inline=False)
    embed.add_field(name="🅱", value=f"{qb}", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    message = await ctx.send(embed=embed, delete_after=30)
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")

@spectraselfbot.command()
async def stopstreaming(ctx):
    await ctx.message.delete()
    await spectraselfbot.change_presence(activity=None, status=discord.Status.dnd)
    embed = discord.Embed(title="stopstreaming", color=0xffffff)
    embed.add_field(name=f"Stopped streaming.", value=f"Make sure to set your stream link in the config.json file!", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30) 

@spectraselfbot.command()
async def discordrules(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Octave selfbot Server Rules...", color=0xffffff)
    embed.add_field(name=f"Dont Be a twat", value=f"is it really that hard to not be a twat", inline=False)
    embed.add_field(name=f"Follow Discord TOS cuz why not", value=f"eh who really cares", inline=False)
    embed.add_field(name=f"Dont spam", value=f"no need to clog up the chat with shit noone gives a fuck about", inline=False)
    embed.add_field(name=f"Dont self promo (Without permision)", value=f"nobody cares about your shit go self promo some where else", inline=False)
    embed.add_field(name=f"Dont bother trying to ping @everyone or @here roles", value=f"you dont have permision too anyway so no need to try retard", inline=False)
    embed.add_field(name=f"If thow decides to break shall given rules, thow shall recive a penalty", value=f"use common sense. admins will take appropriate actions if needed", inline=False)
    embed.add_field(name=f"Octave selfbot and Kacper are hot.", value=f"say other wise and you will get magicaly raped by 12 black guys.", inline=False) 
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30) 

@spectraselfbot.command()
async def tos(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 TOS", color=0xffffff)
    embed.add_field(name=f"This program is for educational purpouses only", value=f"mm yes very educational :wink:", inline=False)
    embed.add_field(name=f'Dont claim that this program is a "token logger" or does any malicious damages without proof.', value=f"you just sound stupid, if you really think 𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁 does anything malicious then prove it :skull:", inline=False)
    embed.add_field(name=f"By using Octave selfbot you understand that you are at risk of getting your discord account banned (just as any other selfbot).", value=f"if you get banned dont complain in my dms or ill fuck your dog.", inline=False)
    embed.add_field(name=f'Decompile it idc just dont skid it :neutral_face:', value=f"python really isnt hard just learn it.", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30) 

@spectraselfbot.command()
async def genpass(ctx, length: int): 
    await ctx.message.delete()
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} genpass"+Fore.RESET)
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    embed = discord.Embed(title="Password generator", color=0xffffff)
    embed.add_field(name=f"Password generated:", value=f"`{code}`", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30)                                                                                       

@spectraselfbot.command()
async def download(ctx):
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} download"+Fore.RESET)
    embed = discord.Embed(title="download", color=000000)
    embed.add_field(name=f"Press the bellow hyperlink to download 𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁.", value=f"[Press here](https://anonfiles.com/J39fr9zfud/Octave selfbot-selfbot-public-release_zip \"J39fr9zfud/Octave selfbot-selfbot-public-release_zip\")", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30) 

@spectraselfbot.command() 
async def whois(ctx, *, user: discord.User = None): 
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} whois"+Fore.RESET)
    user = ctx.author if not user else user
    if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
        embed = discord.Embed(title=f"whois {user}", color=0xffffff)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name=f"User ID:", value=f"{user.id}", inline=False)
        embed.add_field(name=f"Username:", value=f"{user.display_name}", inline=False)
        embed.add_field(name=f"Created At:", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name=f"Bot user:", value=user.bot, inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 
        
    else:
        roles = [role for role in user.roles]
        embed = discord.Embed(title=f"whois {user}", color=0xffffff)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name=f"User ID:", value=f"{user.id}", inline=False)
        embed.add_field(name=f"Username:", value=f"{user.display_name}", inline=False)
        embed.add_field(name=f"Created At:", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name=f"Joined At:", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name=f"Bot user:", value=user.bot, inline=False)
        embed.add_field(name=f"Top Role:", value=user.top_role.mention, inline=False)
        embed.add_field(name=f"Roles: ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 
 
            

@spectraselfbot.command() 
async def hitler(ctx): 
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} hitler"+Fore.RESET)
    responses = [
      "https://media.discordapp.net/attachments/852684092289449984/855141663529369610/hitler_97.png",
"https://media.discordapp.net/attachments/852684092289449984/855141669938003968/hitler_2.png",
"https://media.discordapp.net/attachments/852684092289449984/855141668638687242/hitler_1.png",
"https://media.discordapp.net/attachments/852684092289449984/855141670919471114/hitler_3.png",
"https://media.discordapp.net/attachments/852684092289449984/855141674032037928/hitler_5.png",
"https://media.discordapp.net/attachments/852684092289449984/855141705459302470/hitler_8.png",
"https://media.discordapp.net/attachments/852684092289449984/855141707377016863/hitler_14.png",
"https://media.discordapp.net/attachments/852684092289449984/855141705992372234/hitler_17.png",
"https://media.discordapp.net/attachments/852684092289449984/855141749881569310/hitler_36.png",
"https://media.discordapp.net/attachments/852684092289449984/855141751031595049/hitler_8.png",
"https://media.discordapp.net/attachments/852684092289449984/855141793444528168/hitler_46.png",
"https://media.discordapp.net/attachments/852684092289449984/855141817086509066/hitler_34.png",
"https://media.discordapp.net/attachments/852684092289449984/855141819272527892/hitler_40.png",
"https://media.discordapp.net/attachments/852684092289449984/855141820186099732/hitler_44.png",
"https://media.discordapp.net/attachments/852684092289449984/855141836577308682/hitler_43.png",
"https://media.discordapp.net/attachments/852684092289449984/855141840071819284/hitler_45.png",
"https://media.discordapp.net/attachments/852684092289449984/855141840294379530/hitler_30.png",
"https://cdn.discordapp.com/attachments/852684092289449984/855141840071819284/hitler_45.png",
    ]
    linkz = random.choice(responses)
    embed = discord.Embed(title="Hitler", color=0xffffff)
    embed.add_field(name="Picture of hitler!", value=f"kacper asked for this lmao", inline=False)
    embed.set_image(url=linkz)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30) 

@spectraselfbot.command()
async def delwebhook(ctx, webhook):
    await ctx.message.delete()
    os.system(f'curl -X DELETE {webhook}')
    embed = discord.Embed(title="delwebhook", color=0xffffff)
    embed.add_field(name="Deleted webhook.", value=webhook, inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30) 
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} delwebhook"+Fore.RESET)
    
@spectraselfbot.command() 
async def ppsize(ctx, *, user: discord.User = None):
    await ctx.message.delete()
    responses = [
      "0.1 Inches",
"0.3 Inches",
"0.5 Inches",
"0.8 Inches",
"0.9 Inches",
"2 Inches",
"3 Inches",
"4 Inches",
"6 Inches",
"7 Inches",
"8 Inches",
"9 Inches",
"10 Inches",
"11 Inches",
"12+ Inches",
    ]
    answertopp = random.choice(responses)
    if user == None:
        embed = discord.Embed(title="ppsize", color=0xffffff)
        embed.add_field(name=f"{ctx.author}'s pp is {answertopp} long!", value=f"Pee Pee Poo Poo :weary:", inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} ppsize"+Fore.RESET)  
    else:
        embed = discord.Embed(title="ppsize", color=0xffffff)
        embed.add_field(name=f"{user}'s pp is {answertopp} long!", value=f"Pee Pee Poo Poo :weary:", inline=False)
        embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=30) 
        time = datetime.datetime.now().strftime("%H:%M %p") 
        print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} ppsize"+Fore.RESET) 
    
@spectraselfbot.command() 
async def hack(ctx, user: discord.User = None):
    await ctx.message.delete()
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} hack"+Fore.RESET) 
    gender = ["Male", "Female", "Trans", "Non-Binary", "Gender-Fluid"  "Other"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "DOctave selfbotr", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")


@spectraselfbot.command() 
async def dadjoke(ctx): 
    await ctx.message.delete()
    responses = [
      "What do you call a factory that makes okay products?" "A satisfactory.",
"What did the janitor say when he jumped out of the closet?" "Supplies!",
"Have you heard about the chocolate record player? It sounds pretty sweet.",
"What did the ocean say to the beach?" "Nothing, it just waved.",
"Why do seagulls fly over the ocean?" "Because if they flew over the bay, we'd call them bagels.",
"I only know 25 letters of the alphabet. I don't know y.",
"What did one wall say to the other?" "I'll meet you at the corner.",
"What did the zero say to the eight?" "That belt looks good on you.",
"A skeleton walks into a bar and says, 'Hey, bartender. I'll have one beer and a mop.'",
"Where do fruits go on vacation?" "Pear-is!",
"I asked my dog what's two minus two. He said nothing.",
"What did Baby Corn say to Mama Corn?" "Where's Pop Corn?",
"What's the best thing about Switzerland?" "I don't know, but the flag is a big plus.",
"What does a sprinter eat before a race?" "Nothing, they fast!",
"Where do you learn to make a banana split?" "Sundae school.",
"Dad, did you get a haircut?" "No, I got them all cut!",
"What do you call a poor Santa Claus?" "St. Nickel-less.",
"I got carded at a liquor store, and my Blockbuster card accidentally fell out. The cashier said never mind.",
"Where do boats go when they're sick?" "To the boat doc.",
"I don't trust those trees. They seem kind of shady.",
"My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right!",
"How do you get a squirrel to like you? Act like a nut.",
"Why don't eggs tell jokes? They'd crack each other up.",
"I don't trust stairs. They're always up to something.",
"What do you call someone with no body and no nose? Nobody knows.",
"Did you hear the rumor about butter? Well, I'm not going to spread it!",
"Why couldn't the bicycle stand up by itself? It was two tired.",
"Why did Billy get fired from the banana factory? He kept throwing away the bent ones.",
"Dad, can you put my shoes on?" "No, I don't think they'll fit me.",
"Why can't a nose be 12 inches long? Because then it would be a foot.",
"What does a lemon say when it answers the phone?" "Yellow!",
"This graveyard looks overcrowded. People must be dying to get in.",
"What kind of car does an egg drive?" "A yolkswagen.",
"Dad, can you put the cat out?" "I didn't know it was on fire.",
"How do you make 7 even?" "Take away the s.",
"How does a taco say grace?" "Lettuce pray.",
"What time did the man go to the dentist? Tooth hurt-y.",
"Why didn't the skeleton climb the mountain?" "It didn't have the guts.",
"How many tickles does it take to make an Octave selfbotpus laugh? Ten tickles.",
"I have a joke about chemistry, but I don't think it will get a reaction.",
"What concert costs just 45 cents? 50 Cent featuring Nickelback!",
"What does a bee use to brush its hair?" "A honeycomb!",
"How do you make a tissue dance? You put a little boogie in it.",
"Why did the math book look so sad? Because of all of its problems!",
"What do you call cheese that isn't yours? Nacho cheese.",
"My dad told me a joke about boxing. I guess I missed the punch line.",
"What kind of shoes do ninjas wear? Sneakers!",
"How does a penguin build its house? Igloos it together.",
"You think swimming with sharks is expensive? Swimming with sharks cost me an arm and a leg.",
"I ordered a chicken and an egg from Amazon. I'll let you know...",
"Do you wanna box for your leftovers?" "No, but I'll wrestle you for them.",
"That car looks nice but the muffler seems exhausted.",
"Shout out to my fingers. I can count on all of them.",
"If a child refuses to nap, are they guilty of resisting a rest?",
"What country's capital is growing the fastest?" "Ireland. Every day it's Dublin.",
"I once had a dream I was floating in an ocean of orange soda. It was more of a fanta sea.",
"Did you know corduroy pillows are in style? They're making headlines.",
"Did you hear about the kidnapping at school? It's okay, he woke up.",
"A cheeseburger walks into a bar. The bartender says, 'Sorry, we don't serve food here.'",
"I once got fired from a canned juice company. Apparently I couldn't concentrate.",
"I used to play piano by ear. Now I use my hands.",
"Have you ever tried to catch a fog? I tried yesterday but I mist.",
"I'm on a seafood diet. I see food and I eat it.",
"Why did the scarecrow win an award? Because he was outstanding in his field.",
"I made a pencil with two erasers. It was pointless.",
"How do you make a Kleenex dance? Put a little boogie in it!",
"I'm reading a book about anti-gravity. It's impossible to put down!",
"Did you hear about the guy who invented the knock-knock joke? He won the 'no-bell' prize.",
"I've got a great joke about construction, but I'm still working on it.",
"I used to hate facial hair...but then it grew on me.",
"I decided to sell my vacuum cleaner—it was just gathering dust!",
"I had a neck brace fitted years ago and I've never looked back since.",
"You know, people say they pick their nose, but I feel like I was just born with mine.",
"What's brown and sticky? A stick.",
"Why can't you hear a psychiatrist using the bathroom? Because the 'P' is silent.",
"What do you call an elephant that doesn't matter? An irrelephant.",
"What do you get from a pampered cow? Spoiled milk.",
"I like telling Dad jokes. Sometimes he laughs!",
"What's the best smelling insect?" "A deodor-ant.",
"I used to be a personal trainer. Then I gave my too weak notice.",
"Did I tell you the time I fell in love during a backflip? I was heels over head!",
"If a child refuses to sleep during nap time, are they guilty of resisting a rest?",
"I ordered a chicken and an egg online. I’ll let you know.",
"It takes guts to be an organ donor.",
"If you see a crime at an Apple Store, does that make you an iWitness?",
"I'm so good at sleeping, I can do it with my eyes closed!",
"I was going to tell a time-traveling joke, but you guys didn't like it.",
"Why is Peter Pan always flying?" "He neverlands.",
"How can you tell if a tree is a dogwood tree?" "By its bark.",
"I used to hate facial hair, but then it grew on me.",
"It's inappropriate to make a 'dad joke' if you're not a dad. It's a faux pa.",
"What do you call a hot dog on wheels?" "Fast food!",
"Did you hear about the circus fire? It was in tents.",
"Can February March? No, but April May!",
"How do lawyers say goodbye? We'll be suing ya!",
"Wanna hear a joke about paper? Never mind—it's tearable.",
"What's the best way to watch a fly fishing tournament? Live stream.",
"Spring is here! I got so excited I wet my plants.",
"I could tell a joke about pizza, but it's a little cheesy.",
"Don't trust atoms. They make up everything!",
"When does a joke become a dad joke? When it becomes apparent.",
"I wouldn't buy anything with velcro. It's a total rip-off.",
"What’s an astronaut’s favorite part of a computer? The space bar.",
"I don't play soccer because I enjoy the sport. I'm just doing it for kicks!",
"Why are elevator jokes so classic and good? They work on many levels.",
"Why do bees have sticky hair? Because they use a honeycomb.",
"What do you call a fake noodle? An impasta.",
"Which state has the most streets? Rhode Island.",
"What did the coffee report to the police? A mugging.",
"What did the fish say when he hit the wall? Dam.",
"Is this pool safe for diving? It deep ends.",
    ]
    answer = random.choice(responses)
    embed = discord.Embed(title="dadjoke", color=0xffffff)
    embed.add_field(name=f"Heres a dad joke:", value=f"{answer}", inline=False)
    embed.set_footer(text="𝗦𝗽𝗲𝗰𝘁𝗿𝗮 𝘀𝗲𝗹𝗳𝗯𝗼𝘁", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=30) 
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} dadjoke"+Fore.RESET) 
        
@spectraselfbot.command() 
async def nitro(ctx): 
    await ctx.message.delete()
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    await ctx.send(f"https://discord.gift/{code}")
    time = datetime.datetime.now().strftime("%H:%M %p") 
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{time}{Fore.MAGENTA}] [{Fore.BLUE}√{Fore.MAGENTA}] {Fore.WHITE}Command ran {Fore.MAGENTA}|{Fore.WHITE} nitro"+Fore.RESET) 

if config.get("saved") == False:
    rpc.update(details=f'Setting up Spectra', large_image='s', large_text='Spectra', buttons=[{"label": "Spectra Discord Server", "url": "https://discord.gg/octo"}, {"label": "Spectra Repository", "url":"https://github.com/Spectra-Selfbot/spectra"}], start=time.time())
    print(f"{Fore.MAGENTA}[{Fore.WHITE}SETUP{Fore.MAGENTA}]{Fore.WHITE} Enter your desired prefix below. {Fore.MAGENTA}")
    prefix = input("$ ")
    if len(prefix) > 1:
        print(f"{Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.WHITE} Your prefix can be a maximum of one character long.")
        os.system("pause>nul")
        sys.exit()
    else:
        try:
            config.update({"prefix":prefix})
            with open('config.json', 'w') as f:
                json.dump(config, f, indent=4)
            print(f"{Fore.MAGENTA}[{Fore.WHITE}SETUP{Fore.MAGENTA}]{Fore.WHITE} Enter your authorization token below.{Fore.MAGENTA}")
            token = input("$ ")
            try:
                config.update({"token":token, "saved":True})
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                spectraselfbot.run(token, bot=False, reconnect=True)

            except discord.errors.LoginFailure:
                config.update({"token":"", "saved":False})
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                print(f"{Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.WHITE} Failed connecting to token, please make sure you have entered it in correctly and it is a valid token.")
                os.system("pause>nul")
                sys.exit()
        except:
            print(f"{Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.WHITE} Failed to write to config.json")
            os.system("pause>nul")
            sys.exit()
elif config.get("saved") == True:
    try:
        rpc.update(details='Using Spectra Selfbot', large_image='s', large_text='Spectra', buttons=[{"label": "Spectra Discord Server", "url": "https://discord.gg/octo"}, {"label": "Spectra Repository", "url":"https://github.com/Spectra-Selfbot/spectra"}], start=time.time())
        spectraselfbot.run(config.get("token"), bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.WHITE} Failed connecting to token, please make sure you have entered it in correctly and it is a valid token.")
        os.system("pause>nul")
        sys.exit()
else:
    rpc.update(details=f'Setting up Spectra', large_image='s', large_text='Spectra', buttons=[{"label": "Spectra Discord Server", "url": "https://discord.gg/octo"}, {"label": "Spectra Repository", "url":"https://github.com/Spectra-Selfbot/spectra"}], start=time.time())
    print(f"{Fore.MAGENTA}[{Fore.WHITE}SETUP{Fore.MAGENTA}]{Fore.WHITE}  Enter your desired prefix below. {Fore.MAGENTA}")
    prefix = input("$ ")
    if len(prefix) > 1:
        print(f"{Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.WHITE} Your prefix can be a maximum of one character long.")
        os.system("pause>nul")
        sys.exit()
    else:
        try:
            config.update({"prefix":prefix})
            with open('config.json', 'w') as f:
                json.dump(config, f, indent=4)
            print(f"{Fore.MAGENTA}[{Fore.WHITE}SETUP{Fore.MAGENTA}]{Fore.WHITE} Enter your authorization token below.{Fore.MAGENTA}")
            token = input("$ ")
            try:
                config.update({"token":token, "saved":True})
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                spectraselfbot.run(token, bot=False, reconnect=True)

            except discord.errors.LoginFailure:
                config.update({"token":"", "saved":False})
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                print(f"{Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.WHITE} Failed connecting to token, please make sure you have entered it in correctly and it is a valid token.")
                os.system("pause>nul")
                sys.exit()
        except:
            print(f"{Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.WHITE} Failed to write to config.json")
            os.system("pause>nul")
            sys.exit()
