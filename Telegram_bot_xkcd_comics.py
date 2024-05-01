import os
import telegram

from dotenv import load_dotenv
from Download_random_comics import download_comics


def bot_post(chat_id, bot, comics_filename,  comment):
    with open(comics_filename, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption=comment)


def main():
    load_dotenv()
    chat_id = os.environ['XKCD_COMICS_CHAT_ID']
    bot_token = os.environ['XKCD_COMICS_BOT_TOKEN']
    bot = telegram.Bot(bot_token)
    comics_filename, comment = download_comics()
    bot_post(chat_id, bot, comics_filename,  comment)
    os.remove(comics_filename)


if __name__ == '__main__':
    main()
