# arxiv-downloader

## 環境構築


python 3.6.2
pandas 0.24.1(pandasのバージョンが0.2５の場合にはエラーがでる)

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

`slackbot_setting.py`

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



止める時
```
control + c
```

## bot_channelを追加する

#### slack側の実装

1. slackのチャンネルを作成する
2. チャンネルをクリックしてアプリの追加を選択
3. Bethe_ansatzを選択

#### コード側の実装

1. 
