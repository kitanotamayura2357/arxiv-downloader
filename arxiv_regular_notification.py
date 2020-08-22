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

    def search_today_paper_topic_word(self, topic_word):
        """
        topic_wordはsummaryの中の単語
        """
        print("date")
        print(self.date)

        submittedDate = f'submittedDate:[{self.date.year}{self.date.month}{self.date.day-10} TO {self.date.year}{self.date.month}{self.date.day-3}]'
        updatedDate = f'updatedDate:[{self.date.year}{self.date.month}{self.date.day-10} TO {self.date.year}{self.date.month}{self.date.day}]'

        summary_word = f'abs: "{topic_word}"'
        paper_list = arxiv.query(query=f'{submittedDate} AND {summary_word}')
        
        # length_paper_list = len(paper_list)

        for paper in paper_list:
            print("title:",paper.get('title'))
            print("authors",paper.get('authors'))
            print("submit:",paper.get('published'))
            print("update:",paper.get('updated'))

        return paper_list

    def search_today_paper_author(self, author):

        submittedDate = f'submittedDate:[{self.date.year}{self.date.month}{self.date.day-10} TO {self.date.year}{self.date.month}{self.date.day-3}]'
        updatedDate = f'updatedDate:[{self.date.year}{self.date.month}{self.date.day-10} TO {self.date.year}{self.date.month}{self.date.day}]'

        authors = f'au:"{author}"'
        paper_list = arxiv.query(query=f'{submittedDate} AND {authors}')

        for paper in paper_list:
            print("title",paper.get('title'))
            print("authors",paper.get('authors'))
            print("submit",paper.get('published'))
            print("update",paper.get('updated'))
        return paper_list

    def search_today_paper(self, word, condition="topic_word"):

        submittedDate = f'submittedDate:[{self.date.year}{self.date.month}{self.date.day-10} TO {self.date.year}{self.date.month}{self.date.day-3}]'
        updatedDate = f'updatedDate:[{self.date.year}{self.date.month}{self.date.day-10} TO {self.date.year}{self.date.month}{self.date.day}]'
        print(submittedDate)
        print(word)

        paper_list = []

        if condition == "author":
            authors = f'au:"{word}"'
            pre_paper_list = arxiv.query(query=f'{authors}', sort_by='submittedDate')
        else:
            summary_word = f'abs: "{word}"'
            pre_paper_list = arxiv.query(query=f'{summary_word}', max_results=10, sort_by='submittedDate')
        for paper in pre_paper_list:
            if [self.date.year,
                self.date.month,
                self.date.day-3] == [paper["updated_parsed"][0],
                                     paper["updated_parsed"][1],
                                     paper["updated_parsed"][2]]:
                paper_list.append(paper)

        for paper in paper_list:
            print("title", paper.get('title'))
            print("submit", paper.get('published'))
            print("update", paper.get('updated'))
        return paper_list
