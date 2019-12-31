# -*- coding: utf-8 -*-

from slacker import Slacker
import slackbot_settings

if __name__ == '__main__':
    slack = Slacker(slackbot_settings.API_TOKEN)
    slack.chat.post_message(
        'bot-test-channel',
        'こんにちわー',
        username='ボッサン',
        icon_emoji=':simple_smile:',
        )