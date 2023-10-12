# Slackbot_py
# Slack Bot with Flask and Slack SDK

This is a straightforward Slack bot built with Flask and the Slack SDK. The bot listens for messages in a Slack channel and echoes them back to the same channel.

## Project Description

This project serves as a starting point for creating custom Slack bots using Python. It showcases the integration of Flask and the Slack SDK to handle incoming messages and respond accordingly. The provided example echoes messages, but you can easily extend and customize the bot's functionality to suit your needs.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask
- slack-sdk
- slackeventsapi

You can install the dependencies using:

```bash
pip install Flask slack-sdk slackeventsapi


###Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/your-slack-bot.git
cd your-slack-bot
Install dependencies:

###bash
Copy code
pip install -r requirements.txt
Set up your Slack app:

Create a new Slack app on the Slack API.
Obtain your Bot Token and signing secret.
Update your configuration:

Open config.py and update SLACK_BOT_TOKEN and SIGNING_SECRET with your values.
Running the Bot
Start your Flask app:

bash
Copy code
python your_app_file.py
Expose your local server to the internet using Ngrok:

bash
Copy code
ngrok http 5000
Copy the Ngrok URL (e.g., https://your-ngrok-subdomain.ngrok.io).

Configure your Slack app:

Go back to your Slack app settings and update the "Event Subscriptions" with the Ngrok URL followed by /slack/events (e.g., https://your-ngrok-subdomain.ngrok.io/slack/events).
Subscribe to the message event.
Restart your Flask app.

###Usage
Your Slack bot is now ready to echo messages in the configured channel. Simply mention the bot or send a message, and it will respond.

Feel free to customize the bot's behavior in the handle_message function.
