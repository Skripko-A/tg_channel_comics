import os
from random import randint
from urllib.parse import urlsplit
import requests


def fetch_comics_metadata(comics_number: int) -> dict:
    url = f'https://xkcd.com/{comics_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    payload = response.json()
    return payload


def get_comics_max_number() -> int:
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    payload = response.json()
    comics_max_number = payload['num']
    return comics_max_number


def pick_comics_extension(comics_url: str) -> str:
    path = urlsplit(comics_url).path
    comics_extension = os.path.splitext(path)[1]
    return comics_extension


def download_comics() -> (str, str):
    comics_number: int = randint(0, get_comics_max_number())
    comics_data: dict = fetch_comics_metadata(comics_number)
    author_comics_comment: str = comics_data['alt']
    comics_url: str = comics_data['img']
    comics_title: str = comics_data['title']
    comics_extension: str = pick_comics_extension(comics_url)
    comics_filename: str = f'{comics_number}-{comics_title}xkcd{comics_extension}'
    response = requests.get(comics_url)
    response.raise_for_status()
    with open(comics_filename, 'wb') as file:
        file.write(response.content)
    return comics_filename, author_comics_comment
