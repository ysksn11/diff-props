import json
import urllib.parse
import boto3
import datetime
from datetime import timedelta, timezone
import os
from bs4 import BeautifulSoup
import requests

def lambda_handler(event, context):
    JST = timezone(timedelta(hours=+9), "JST")
    dt_now = datetime.datetime.now(JST)
    date_str = dt_now.strftime("%Y年%m月%d日")

    response = requests.get("https://mainichi.jp/editorial/")

    soup = BeautifulSoup(response.text)
    articles = soup.find_all(class_="articlelist-title")
    for article in articles:
        print(article.get_text())
    # pages = soup.find("ul", class_="lsit_typeD")
    # articles = pages.find_all("article")

    # links = [ "https:" + a.a.get("href") for a in articles if date_str in a.time.text ]
    # print(links)

if __name__ == "__main__":
    lambda_handler("test", "test")
