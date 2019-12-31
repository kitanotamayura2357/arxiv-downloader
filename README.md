# arxiv-downloader

## 環境構築

pandasのインストール  

```
$ pip  pandas
```

arXiv APIのインストール

```
$ pip install arxiv
```

schedule moduleのインストール

```
$ pip install schedule
```

slackbotのインストール

```
$ pip install slackbot
```

API_TOKENを記入

```
API_TOKEN = "XXXX-XXXXXXXXXXXXXX-XXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXX"
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
