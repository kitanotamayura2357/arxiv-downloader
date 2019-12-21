import pprint
import arxiv
import pandas as pd
import time
import argparse
import os
import datetime


class ArxivTodayNotification(object):
    def __init__(self, date):
        self.date = date

    def search_today_paper(self):

        print("date")
        # print(date)
        print(self.date)

        paper_list = arxiv.query(query=f'submittedDate:[{self.date.year}{self.date.month}{self.date.day-4} TO {self.date.year}{self.date.month}{self.date.day-3}]')       
        return paper_list

 


# date = datetime.datetime.now()
# atn = ArxivTodayNotification(date)


#atn = ArxivTodayNotification(date)

# paper_list = atn.search_today_paper()

# print(paper_list)






# dt_now = datetime.datetime.now()




# paper_list = arxiv.query(query=f'submittedDate:[{dt_now.year}{dt_now.month}{dt_now.day-4}{dt_now.hour}{dt_now.minute}{dt_now.second} TO {dt_now.year}{dt_now.month}{dt_now.day-3}{dt_now.hour}{dt_now.minute}{dt_now.second}]')


# print("paper_list_length",len(paper_list))

# num = 1
# for paper in paper_list:
#     print("No.",num)
#     print(paper.get('title'))
#     num = num + 1


#author = "Essler"
#paper_list = arxiv.query(query=f'au:"{author}"')

#print(paper_list)

#print(f'submittedDate:{dt_now.year}{dt_now.month}{dt_now.day}{dt_now.hour}{dt_now.minute}{dt_now.second} TO {dt_now.year}{dt_now.month}{dt_now.day}{dt_now.hour}{dt_now.minute}{dt_now.second}')
#print(f'{dt_now.year}{dt_now.month}{dt_now.day-1}{dt_now.hour}{dt_now.minute}{dt_now.second}')