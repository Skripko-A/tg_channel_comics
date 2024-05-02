import os
import telegram
import glob
from dotenv import load_dotenv
from Download_random_comics import download_comics


def send_photo_by_bot(chat_id: str, bot: telegram.bot.Bot, comics_filename: str,  caption: str):
    with open(comics_filename, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption=caption)


def clear_temp_png_xkcd_files():
    png_files = glob.glob('**/*xkcd.png', recursive=True)
    for png_file in png_files:
        os.remove(png_file)


def main():
    load_dotenv()
    chat_id: str = os.environ['XKCD_COMICS_CHAT_ID']
    bot_token: str = os.environ['XKCD_COMICS_BOT_TOKEN']
    bot: telegram.bot.Bot = telegram.Bot(bot_token)
    try:
        comics_filename, comment = download_comics()
        send_photo_by_bot(chat_id, bot, comics_filename,  comment)
    finally:
        clear_temp_png_xkcd_files()


if __name__ == '__main__':
    main()
