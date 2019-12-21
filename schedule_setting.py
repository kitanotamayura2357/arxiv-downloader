import datetime
import time
import schedule
import arxiv_regular_notification as arn

def job():
    
    date = datetime.datetime.now()




    print("1",date)
    atn = arn.ArxivTodayNotification(date)
    today_paper_list = atn.search_today_paper()


    for today_paper in today_paper_list:
        print("title",today_paper.get('title'))
        print("author",today_paper.get('authors'))
        
    


schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)