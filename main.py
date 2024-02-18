import discord
from discord.ext import commands
import os
import requests
import json
import colorama
from colorama import Fore, Style
import asyncio





# Initialize colorama
colorama.init()

async def show_ciphercord_animation():
    # Display the Ciphercord animation
    for _ in range(5):
        print(Fore.RED + Style.BRIGHT + "    C" + Fore.GREEN + "I" + Fore.YELLOW + "P" + Fore.BLUE + "H" + Fore.MAGENTA + "E" +
              Fore.CYAN + "R" + Fore.RED + "C" + Fore.GREEN + "O" + Fore.YELLOW + "R" + Fore.BLUE + "D" + Fore.WHITE +
              "    ", end="\r")
        await asyncio.sleep(0.2)
        print("             ", end="\r")
        await asyncio.sleep(0.2)
      

    

# Load configuration from config.json
with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['token']
ROLE_NAME = config['role_name']
PREFIX = config['prefix']




bot = commands.Bot(command_prefix=PREFIX,
                  intents=discord.Intents.all(),
                  help_command=None)











@bot.event
async def on_ready():
    await show_ciphercord_animation()
    print("""
  ======================================================
                  Bot is online!
  ======================================================
    """)
    
    


    
@bot.command()
@commands.has_role(ROLE_NAME)
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(
      title='Beach Service',
      description=
      '**BEACH SERVICE HELP MENU**\n `.bhelp`\n **USE THIS COMMAND FOR GET MIDLEMAN AND EXCHANGER COMMAND INFO**'
  )
  await ctx.send(embed=embed)

@bot.command()
@commands.has_role(ROLE_NAME)
async def bhelp(ctx):
  embed = discord.Embed(
      title='Beach Service',
      description=
      '''**GENRAL HELP MENU**
 `.greet` 
 **Use This Command To Greet to User.
 `.ty`
 Use This Command After Completing Deal to Give Thanks Msg 
 `.dtnw` 
 Give This Command To Give Tos and warranty msg 
 `.calc`
 Use This Command to Calculate 
 `.pyn` 
 Use This Command To Give Paynote Message
 `.client` 
 Use This Command To Give Client Role
 `.rminr`
 USE THIS COMMOD AFTER RECEIVED INR AMOUNT
 `.rmcrypto`
 USE THIS COMMAND AFTER RECIEVED CRYPTO MM
 `.bal`
  USE THIS COMMAND TO GET YOU CRYPTO WALLET BALANCE**'''
  )
  await ctx.send(embed=embed)

@bot.command()
@commands.has_role(ROLE_NAME)
async def greet(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Beach Service', description=f'<a:VP_white_hearts:1167381163959140412> **Greetings, {ctx.author.mention} Will be your Middle Man For The Deal , Kindly Drop Dev ID Of Buyer/Seller**')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role(ROLE_NAME)
async def ty(ctx):
    await ctx.message.delete()
    await ctx.send('<:AUI_thanks:1167381632991367258> **Thanks For Choosing Beach Mm Hope To See You Soon . Have A Great Day**')


@bot.command()
@commands.has_role('ONE    N     ONLY      <3')
async def secupi(ctx):
    await ctx.message.delete()
    await ctx.send('yet')

@bot.command()
@commands.has_role('ONE    N     ONLY      <3')
async def secltc(ctx):
    await ctx.message.delete()
    await ctx.send('LY52R7vVEN9y3qoqYeH5y1UiPswKfWmc32')
  
@bot.command()
@commands.has_role(ROLE_NAME)
async def dtnw(ctx):
  await ctx.message.delete()
  embed = discord.Embed(
      title='Beach Service',
      description=
      '<a:monkaTOS:1167382200413601862> **Please Check Deal Info , Confirm your deal , Discuss Tos & Warranty Of That Product . **'
  )
  await ctx.send(embed=embed)

@bot.command()
@commands.has_role(ROLE_NAME)
async def pyn(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title='Beach Service',
        description='''**Paynote is Compulsory to add while making payment if you will not add we will take penalty . 
 Penalty 10 Rs 
 Paynote 
 • For  Fampay users : I have received my products .
 • For other UPI users : I authorized this payment and received my products. **'''
    )
    embed.set_image(url='https://media.discordapp.net/attachments/1020524533209383003/1069262338638749716/PhonePay_-_Copy.png')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role(ROLE_NAME)
async def calc(ctx, *, expression):
    await ctx.message.delete()
    try:
        result = eval(expression)
        embed = discord.Embed(description=f'<:question:1161226041612832868> **Your Question :** {expression}\n **Answer :** {result}')
        await ctx.send(embed=embed)
    except:
        await ctx.send("Invalid expression")

@bot.command()
@commands.has_role('TEAM BEACH')
async def client(ctx, member: discord.Member):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, id=1167447911072808960)
    await member.add_roles(role)
    embed=discord.Embed(description=f'**{member.mention} Has Been Given Client Role.**')

    await ctx.send(embed=embed)

@bot.command()
@commands.has_role(ROLE_NAME)
async def rminr(ctx, amount: str):
    await ctx.message.delete()
    try:

        if '.' not in amount:
            amount += '.00'
        
        embed = discord.Embed(
            title="Beach Service",
            description=f'''**<a:arrow:1167382462133960735> {ctx.author.mention} HAS RECEIVED ₹{amount}
<a:arrow:1167382462133960735> NOW YOU CAN CONTINUE YOUR DEAL.
<a:arrow:1167382462133960735> PING {ctx.author.mention} TO RELEASE **'''
        )
        
        await ctx.send(embed=embed)
    except ValueError:
        await ctx.send("Invalid input. Please provide a valid number.")

@bot.command()
@commands.has_role(ROLE_NAME)
async def rmcrypto(ctx, amount: str):
    await ctx.message.delete()
    try:

        if '.' not in amount:
            amount += '.00'
        
        embed = discord.Embed(
            title="Beach Service",
            description=f'''**<a:arrow:1167382462133960735> {ctx.author.mention} HAS RECEIVED ${amount}
<a:arrow:1167382462133960735> NOW YOU CAN CONTINUE YOUR DEAL.
<a:arrow:1167382462133960735> PING {ctx.author.mention} TO RELEASE **'''
        )
        
        await ctx.send(embed=embed)
    except ValueError:
        await ctx.send("Invalid input. Please provide a valid number.")



@bot.command()
@commands.has_role(ROLE_NAME)
async def bal(ctx, ltcaddress):
    await ctx.message.delete()
        
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')
    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8  
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.send("**Failed to retrieve balance. Please check the Litecoin address.**")
        return

    
    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.send("**Failed to retrieve the current price of Litecoin.**")
        return
    
    
    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price
    
    
    send = f"<:LTC:1167382785212817481> **Total LTC Balance: ${usd_balance:.2f}\n"
    send += f"<:LTC:1167382785212817481> Total LTC Received: ${usd_total_balance:.2f}\n"
    send += f"<:LTC:1167382785212817481> Unconfirmed LTC: ${usd_unconfirmed_balance:.2f}**"
    
    await ctx.send(send)



bot.run(TOKEN)


