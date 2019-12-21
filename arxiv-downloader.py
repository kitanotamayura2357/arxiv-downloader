import pprint
import arxiv
import pandas as pd
import time
import argparse
import os

parser = argparse.ArgumentParser(description='input author')
parser.add_argument('author', help='input author')
args = parser.parse_args()
paper_list = arxiv.query(query=f'au:"{args.author}"')
print("paper_list_length",len(paper_list))
# if paper_list:
#     author_name = args.author.replace(" ","_")
#     arxiv_path = 'downloaded_arxiv_paper'
#     if not os.path.isdir(arxiv_path):
#         os.mkdir(arxiv_path)
#     new_dir_path = f'downloaded_arxiv_paper/{author_name}'
#     if not os.path.isdir(new_dir_path):
#             os.mkdir(new_dir_path)



def get_paper_name(paper):
    authors_name = ','.join(paper.get('authors')).replace(' ', '.')
    paper_id = paper.get('id').split('/')[-1]
    paper_title = paper.get('title').replace('\n','').replace('  ',' ').replace(' ', '_').replace('/','-').replace(':','-').replace('"','').replace(",","_").replace("---","").replace("__","_").replace("$","").replace("\\","").replace("*","").replace("?",'').replace('|','').replace('<','').replace('>','')
    paper_title = f'{paper_title}'
    paper_file_name = paper_id + "." + paper_title + "(" +authors_name +")"
    if len(paper_file_name) > 180:
        paper_file_name = paper_file_name = paper_id + "." + "(" +authors_name +")"
    return paper_file_name



def make_download_directory():
    arxiv_path = 'downloaded_arxiv_paper'
    if not os.path.isdir(arxiv_path):
        os.mkdir(arxiv_path)

def make_author_directory(given_author, authors): 
    for author in authors:
        if given_author in author:
            author_name = author.replace("  "," ").replace(" ","_").replace("._",". ")
            new_dir_path = f'downloaded_arxiv_paper/{author_name}'
            if not os.path.isdir(new_dir_path):
                os.mkdir(new_dir_path)



if paper_list:
    make_download_directory()
    num = 0
    for paper in paper_list:
        num = num + 1
        print("No.",num)
        print("title",paper.get('title'))
        print(paper.get('id').split('/')[-1])
        print(paper.get('authors'))
        authors = paper.get('authors')
        given_author_name = args.author
        print("get_paper_name",get_paper_name(paper))
        make_author_directory(given_author=given_author_name, authors=authors)
        
        #make_author_directory(aut)




    
# num = 0
# for paper in paper_list:
#     num = num + 1
#     print("No.",num)
#     print("title",paper.get('title'))
#     print(paper.get('id').split('/')[-1])
#     print(paper.get('authors'))
#     print("get_paper_name",get_paper_name(paper))
#     arxiv.download(obj=paper, dirpath=f'downloaded_arxiv_paper/{author_name}', slugify=get_paper_name)
#     #arxiv.download(obj=paper, dirpath=f'downloaded_arxiv_paper/{author_name}')
