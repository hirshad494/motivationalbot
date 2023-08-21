import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

bot = discord.Client(intents=discord.Intents.all())

emotion_keywords = ["sad", "depressed", "unhappy", "angry", "disheartened", "downcast", "heartbroken"]

motivational_messages = [
    "Stay strong!",
    "You've got this!",
    "Believe in yourself!",
    "Every setback is a setup for a comeback!"
]

if "is_responding" not in db.keys():
    db["is_responding"] = True

def get_inspiring_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote

def add_motivational_message(new_message):
    if "motivational_messages" in db.keys():
        messages = db["motivational_messages"]
        messages.append(new_message)
        db["motivational_messages"] = messages
    else:
        db["motivational_messages"] = [new_message]

def delete_motivational_message(index):
    messages = db["motivational_messages"]
    if 0 <= index < len(messages):
        removed_message = messages.pop(index)
        db["motivational_messages"] = messages
        return removed_message
    else:
        return None

@bot.event
async def on_ready():
    print('Bot is online and ready to spread positivity!')
    start_message = "Hello! I'm your Motivation Bot, ready to inspire and uplift. Use `$intro` to see what I can do."
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send(start_message)
                break
    print('Start-up message sent.')

@bot.event
async def on_message(message):
    print('Message received:', message.content)
    if message.author == bot.user:
        return

    msg = message.content.lower()

    if msg.startswith('$intro'):
        intro_message = (
            "Hello! I'm your friendly Motivation Bot. Here's what I can do:\n"
            "- Use `$inspire` to get an inspiring quote.\n"
            "- Use `$add [message]` to add a new motivational message.\n"
            "- Use `$delete [index]` to delete a motivational message.\n"
            "- Use `$list` to see the list of motivational messages.\n"
            "- Use `$toggle [on/off]` to toggle emotion-based responses.\n"
            "I can also respond to emotions containing sad keywords!"
        )
        await message.channel.send(intro_message)

    if msg.startswith('$inspire'):
        quote = get_inspiring_quote()
        await message.channel.send(quote)

    if msg.startswith("$add"):
        new_message = msg.split("$add", 1)[1]
        add_motivational_message(new_message)
        await message.channel.send("New motivational message added.")

    if msg.startswith("$delete"):
        if "motivational_messages" in db.keys():
            index = int(msg.split("$delete", 1)[1])
            removed_message = delete_motivational_message(index)
            if removed_message is not None:
                await message.channel.send(f'Removed: {removed_message}')
            else:
                await message.channel.send('Invalid index. Use "$delete [index]" to remove a message.')
        else:
            await message.channel.send('No motivational messages found.')

    if msg.startswith("$list"):
        if "motivational_messages" in db.keys():
            messages = list(db["motivational_messages"])
            messages_str = "\n".join(messages)
            await message.channel.send("List of motivational messages:\n" + messages_str)
        else:
            await message.channel.send("No motivational messages found.")

    if msg.startswith("$toggle"):
        value = msg.split("$toggle", 1)[1]
        if value.lower() == " on":
            db["is_responding"] = True
            await message.channel.send("Responding to emotions is now on.")
        else:
            db["is_responding"] = False
            await message.channel.send("Responding to emotions is now off.")

    if db["is_responding"] and any(keyword in msg for keyword in emotion_keywords):
        available_responses = motivational_messages
        if "motivational_messages" in db.keys():
            available_responses = available_responses + list(db["motivational_messages"])

        await message.channel.send(random.choice(available_responses))

keep_alive()
bot_token = os.environ['BOT_TOKEN']
bot.run(bot_token)
