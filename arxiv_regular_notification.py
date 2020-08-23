import arxiv


class ArxivTodayNotification(object):
    def __init__(self, date):
        self.date = date

    def search_today_paper_topic_word(self, topic_word):
        """
        topic_wordはsummaryの中の単語
        """
        print("date")
        print(self.date)

        summary_word = f'abs: "{topic_word}"'
        paper_list = arxiv.query(query=f'{summary_word}')

        for paper in paper_list:
            print("title:", paper.get('title'))
            print("authors", paper.get('authors'))
            print("submit:", paper.get('published'))
            print("update:", paper.get('updated'))

        return paper_list

    def search_today_paper_author(self, author):

        authors = f'au:"{author}"'
        paper_list = arxiv.query(query=f'{authors}')

        for paper in paper_list:
            print("title", paper.get('title'))
            print("authors", paper.get('authors'))
            print("submit", paper.get('published'))
            print("update", paper.get('updated'))
        return paper_list

    def search_today_paper(self, word, condition="topic_word"):

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
                self.date.day-5] == [paper["updated_parsed"][0],
                                     paper["updated_parsed"][1],
                                     paper["updated_parsed"][2]]:
                paper_list.append(paper)
                print(paper)

        for paper in paper_list:
            print("title", paper.get('title'))
            print("submit", paper.get('published'))
            print("update", paper.get('updated'))
        return paper_list
