import os
from random import randint
from urllib.parse import urlsplit
import requests


def get_comics_json(comics_number):
    url = f'https://xkcd.com/{comics_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    payload_json = response.json()
    return payload_json


def get_comics_max_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    payload_json = response.json()
    comics_max_number = payload_json['num']
    return comics_max_number


def pick_comics_extension(comics_url):
    path = urlsplit(comics_url).path
    comics_extension = os.path.splitext(path)[1]
    return comics_extension


def download_comics():
    comics_number = randint(0, get_comics_max_number())
    comics_json = get_comics_json(comics_number)
    author_comics_comment = comics_json['alt']
    comics_url = comics_json['img']
    comics_title = comics_json['title']
    comics_extension = pick_comics_extension(comics_url)
    comics_filename = f'comics_dir/{comics_number}-{comics_title}{comics_extension}'
    response = requests.get(comics_url)
    response.raise_for_status()
    with open(comics_filename, 'wb') as file:
        file.write(response.content)
    return comics_filename, author_comics_comment
