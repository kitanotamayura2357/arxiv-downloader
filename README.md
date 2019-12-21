# arxiv-downloader

## 環境構築

pandasのインストール  

```
$ pip pandas pandas
```

arXiv APIのインストール

```
$ pip install arxiv
```
## 使い方

以下のコマンドでarXivに上がっているauthor nameの論文を全て自動ダウンロードする
```
$ python arxiv_downloader.py "author name"
```
ダウンロードした論文の名前は
```
arXiv_ID title (author1, author2, ...)
```
になる
