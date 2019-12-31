import os
import arxiv
import logging
import time


class ArxivDownloadManager(object):
    def __init__(self, paper):
        self.paper = paper

    # def get_paper_name(self):
    #     authors_name = ','.join(self.paper.get('authors')).replace(' ', '.')
    #     paper_id = self.paper.get('id').split('/')[-1]
    #     paper_title = self.paper.get('title').replace('\n','').replace('  ',' ').replace(' ', '_').replace('/','-').replace(':','-').replace('"','').replace(",","_").replace("---","").replace("__","_").replace("$","").replace("\\","").replace("*","").replace("?",'').replace('|','').replace('<','').replace('>','')
    #     paper_title = f'{paper_title}'
    #     paper_file_name = paper_id + "." + paper_title + "(" +authors_name +")"
    #     if len(paper_file_name) > 180:
    #         paper_file_name = paper_file_name = paper_id + "." + "(" +authors_name +")"
    #     return paper_file_name

    def get_paper_name(self, obj):
        authors_name = ','.join(obj.get('authors')).replace(' ', '.')
        paper_id = obj.get('id').split('/')[-1]
        paper_title = obj.get('title').replace('\n','').replace('  ',' ').replace(' ', '_').replace('/','-').replace(':','-').replace('"','').replace(",","_").replace("---","").replace("__","_").replace("$","").replace("\\","").replace("*","").replace("?",'').replace('|','').replace('<','').replace('>','')
        paper_title = f'{paper_title}'
        paper_file_name = paper_id + "." + paper_title + "(" +authors_name +")"
        if len(paper_file_name) > 180:
            paper_file_name = paper_file_name = paper_id + "." + "(" +authors_name +")"
        print("paper_file_name",paper_file_name) 
        return paper_file_name

  
    def make_download_directory(self):
        arxiv_path = 'downloaded_arxiv_paper'
        if not os.path.isdir(arxiv_path):
            os.mkdir(arxiv_path)


    def make_author_directory(self):
        # paper_file_name = self.get_paper_name()
        author_dir_paths = []
        authors = self.paper.get('authors')
        for author in authors:
            author_name = author.replace("  "," ").replace(" ","_").replace("._",". ")
            new_dir_path = f'downloaded_arxiv_paper/{author_name}'
            author_dir_paths.append(new_dir_path)
            if not os.path.isdir(new_dir_path):
                os.mkdir(new_dir_path)
        return author_dir_paths


    def custom_slugify(self, obj):
        print("test",obj.get('id').split('/')[-1])
        return obj.get('id').split('/')[-1]


    def paper_download(self):
        # paper_name = self.get_paper_name()
        self.make_download_directory()
        author_dir_paths = self.make_author_directory()
        print("author_dir_paths",author_dir_paths)
        for author_dir_path in author_dir_paths:
            try:
                arxiv.download(obj=self.paper, dirpath=f'{author_dir_path}',slugify=self.get_paper_name)
                print("author_dir_path:",author_dir_path)
                time.sleep(3)
            except Exception as e:
                logging.warning(f"download_error {e}")
                time.sleep(3)
            # arxiv.download(obj=self.paper, dirpath=f'downloaded_arxiv_paper/{author_name}',slugify=self.get_paper_name)
            # arxiv.download(obj=self.paper, slugify=self.custom_slugify)