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

if paper_list:
    author_name = args.author.replace(" ","_")
    arxiv_path = 'downloaded_arxiv_paper'
    if not os.path.isdir(arxiv_path):
        os.mkdir(arxiv_path)
    new_dir_path = f'downloaded_arxiv_paper/{author_name}'
    if not os.path.isdir(new_dir_path):
            os.mkdir(new_dir_path)

def get_paper_name(paper):
    use_char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ%&():;? "
    authors_name = ','.join(paper.get('authors')).replace(' ', '.')
    paper_id = paper.get('id').split('/')[-1]
    paper_title = paper.get('title').replace('\n','').replace('  ',' ').replace(' ', '_').replace('/','-').replace(':','-').replace('"','').replace(",","_").replace("---","").replace("__","_").replace("$","").replace("\\","").replace("*","").replace("?",'').replace('|','').replace('<','').replace('>','')
    paper_title = f'{paper_title}'
    paper_file_name = paper_id + "." + paper_title + "(" +authors_name +")"
    aa = len('1611.05794v3.Sensitivity_of_quantum_walks_to_boundary_of_two-dimensional_lattices-_approaches_from_the_CGMV_method_and_topological_phases(Takako.Endo,Norio.Konno,Hideaki.Obuse,Etsuo.Segawa).pdf')
    print("aa",aa)
    if len(paper_file_name) > 180:
        paper_file_name = paper_file_name = paper_id + "." + "(" +authors_name +")"
    return paper_file_name

    
num = 0
for paper in paper_list:
    num = num + 1
    print("No.",num)
    print("title",paper.get('title'))
    print(paper.get('id').split('/')[-1])
    print(paper.get('authors'))
    print("get_paper_name",get_paper_name(paper))
    arxiv.download(obj=paper, dirpath=f'downloaded_arxiv_paper/{author_name}', slugify=get_paper_name)
    #arxiv.download(obj=paper, dirpath=f'downloaded_arxiv_paper/{author_name}')
