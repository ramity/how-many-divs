FROM python:3.11

WORKDIR /root/src

RUN apt update

RUN pip install --upgrade pip
RUN pip install beautifulsoup4
RUN pip install pandas
RUN pip install matplotlib
RUN pip install pytest-playwright
RUN playwright install-deps
RUN playwright install

ENTRYPOINT sleep infinity
