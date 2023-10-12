from slack_sdk.web import WebClient
from slackeventsapi import SlackEventAdapter
from flask import Flask
import os

SLACK_BOT_TOKEN = 'xoxb-5985321298165-5994324832354-P8rjL9J0i0DAqLZqh5VquZ1a'

app = Flask(__name__)
slack_client = WebClient(token=SLACK_BOT_TOKEN)
slack_events_adapter = SlackEventAdapter(
    '4ed7da8305820a59553a24a5b0e97afa', '/slack/events', app)


@slack_events_adapter.on('message')
def handle_message(event_data):
    message = event_data['event']

    if message.get('subtype') is None and message.get('user') != slack_client.api_call('auth.test')['user_id']:
        channel_id = message['channel']
        user = message['user']
        text = message['text']

        slack_client.chat_postMessage(
            channel=channel_id, text=f"{text}")


if __name__ == '__main__':
    app.run(debug=True)
