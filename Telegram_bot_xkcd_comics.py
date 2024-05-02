import os
import telegram

from dotenv import load_dotenv
from Download_random_comics import download_comics


def send_photo_by_bot(chat_id: str, bot: telegram.bot.Bot, comics_filename: str,  caption: str):
    with open(comics_filename, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption=caption)


def main():
    load_dotenv()
    chat_id: str = os.environ['XKCD_COMICS_CHAT_ID']
    bot_token: str = os.environ['XKCD_COMICS_BOT_TOKEN']
    bot: telegram.bot.Bot = telegram.Bot(bot_token)
    comics_filename, comment = download_comics()
    send_photo_by_bot(chat_id, bot, comics_filename,  comment)
    os.remove(comics_filename)


if __name__ == '__main__':
    main()
