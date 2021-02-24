ARG BASE_IMAGE=python:3.6-buster
FROM $BASE_IMAGE

RUN pip install \
    pandas==0.24.1 \
    arxiv \
    schedule \
    slackbot \
    && pip cache purge

RUN mkdir /arxiv_downloader
WORKDIR /arxiv_downloader

COPY slackbot *.py ./

ENTRYPOINT [ "python" ]
CMD [ "arxiv-downloader.py", "Albert Einstein" ]