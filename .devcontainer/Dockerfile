# ベースImageの取得
FROM python:3.8-buster

# Pythonのパッケージ
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
#ADD ./backend /app