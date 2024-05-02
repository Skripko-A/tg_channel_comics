# Телеграм бот засылает комиксы xkcd
Бот для телеграм. Скачивает и постит один [xkcd](https://xkcd.com/) (веб-комикс).
### Как установить
Для работы скриптов вам понадобится телеграм бот.
Создать бота в телеграм:  
@BotFather (https://t.me/BotFather)
```
/start
```
```
/newbot
```
Сохраните токен вашего бота и chat_id вашего телеграм канала в .env файл:
```
XKCD_COMICS_BOT_TOKEN = 'токен вашего телеграм бота'
XKCD_COMICS_CHAT_ID = 'chat_id вашего телеграм канала'
```
Python3 должен быть уже установлен.  
Установите зависимости:
```commandline
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```
### Пример запуска скриптов
Данный репо содержит 2 скрипта.
Скрипт Telegram_bot_xkcd_comics.py используя набор функций скрипта Download_random_comics.py скачивает комикс со случайно сгенерированным номером. Скачанный в виде картинки png комикс подхватывается ботом и отправляется в телеграм, после чего скачанный файл удаляется.
```commandline
source env/bin/activate
python3 Telegram_bot_xkcd_comics.py
```
![](https://github.com/Skripko-A/tg_channel_comics/blob/master/xkcd_comics_bot_chat.png)

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
