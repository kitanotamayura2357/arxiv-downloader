from slackbot import bot_post as bp
import datetime
import time
import schedule
import arxiv_regular_notification as arn
import arxiv_download_manager as adm


def post_paper_to_slack(date, word, condition="topic_word", slack_channel="bot-test-channel"):

    atn = arn.ArxivTodayNotification(date)
    today_paper_list = atn.search_today_paper(word=word, condition=condition)
    bp.post_paper_list(today_paper_list=today_paper_list, slack_channel=slack_channel)
    for paper in today_paper_list:
        adma = adm.ArxivDownloadManager(paper)
        adma.paper_download()
        time.sleep(1)


def job():

    date = datetime.datetime.now()
    post_paper_to_slack(date=date,
                        word="Bethe",
                        condition="topic_word",
                        slack_channel="bot_arxiv_bethe_ansatz")
    post_paper_to_slack(date=date,
                        word="tensor network",
                        condition="topic_word",
                        slack_channel="bot_arxiv_tensor_network")
    post_paper_to_slack(date=date,
                        word="quantum annealing",
                        condition="topic_word",
                        slack_channel="bot_arxiv_quantum_annealing")


# 毎日定時に実行
schedule.every().day.at("10:00").do(job)


print("start")
while True:
    schedule.run_pending()
    time.sleep(1)



