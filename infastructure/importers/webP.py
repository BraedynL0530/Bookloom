from core.classes.Book import Book
from bs4 import BeautifulSoup as BS
import os
import requests
def download_concurrent(url, concurrency=3):
    id = 0
    for i in range(concurrency):
        id += 1
        download_chapter(url, id)
    return

def download_chapter(url, id=0):
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    Headers ={
        "User-Agent": agent,
        "referer": url
    }
    title = "temp" #fetch from url/something else
    index = id
    output = f"{title}{index}.cbz"

def find_images():
    return

#plugin file saving,