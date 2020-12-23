#!/usr/bin/env python3
from config import config
from telebot import TeleBot
from tpblite import TPB
import json


def main():
    bot = TeleBot(config.get_api_key(), parse_mode=None)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "eh yo")

    @bot.message_handler(commands=['search'])
    def search_torrents(message):
        chat_id = message.chat.id
        tpb = TPB('https://tpb.party')
        text = message.text.replace('/search ', '')
        torrents_list = tpb.search(text, page=1)[0:config.get_results_limit()]
        for torrent in torrents_list:
            bot.send_message(chat_id, torrent.title)

    bot.polling()

if __name__ == '__main__':
    main()
