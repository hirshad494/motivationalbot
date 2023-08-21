# Motivation Bot

Motivation Bot is a Discord bot designed to inspire and uplift users by providing motivational messages and quotes. The bot can also respond to messages containing sad emotion keywords, offering words of encouragement.

## Features

- Get an inspiring quote using the `$inspire` command.
- Add your own motivational messages using the `$add [message]` command.
- Delete a motivational message using the `$delete [index]` command.
- List all stored motivational messages using the `$list` command.
- Toggle emotion-based responses on or off using the `$toggle [on/off]` command.
- Responds to emotions containing sad keywords with motivational messages.

## Setup and Usage

1. Install the required dependencies using the following command:

pip install discord.py flask

2. Set up your bot on the Discord Developer Portal and retrieve your bot token.

3. Create a `.env` file in the project directory and add your bot token:
   
BOT_TOKEN=your_bot_token_here

4. Run the bot by executing the main Python script:

python main.py

5. Invite your bot to your Discord server and start using its commands.

## Keep the Bot Alive

The `keep_alive.py` script provides a simple web server to keep your bot alive, especially on platforms that require continuous activity.

To keep the bot online, use the following steps:

1. Add the `keep_alive.py` script to your project directory.

2. Import the `keep_alive` function in your main script:
```python
from keep_alive import keep_alive

1. Call the keep_alive() function before running the bot:
keep_alive()

Remember to replace placeholders like `your_bot_token_here` with actual values. You can also add more details about your bot, its commands, and any other information you'd like to provide to users.

