from slacker import Slacker
from slackbot import slackbot_settings

import time


def post_paper_list(today_paper_list, slack_channel):

    slack = Slacker(slackbot_settings.API_TOKEN)
    for today_paper in today_paper_list:
        title = today_paper.get('title')
        author = today_paper.get('authors')
        paper_id = today_paper.get('id')
        slack.chat.post_message(slack_channel, f'title {title},\n author {author},\n url {paper_id}', as_user=True)
        time.sleep(1)
    slack.chat.post_message(slack_channel, f'Number of papers {len(today_paper_list)}', as_user=True)
