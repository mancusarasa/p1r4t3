#!/usr/bin/env python3
from telebot import TeleBot
from config import config


def main():
    bot = TeleBot(config.get_api_key(), parse_mode=None)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "eh yo")

    bot.polling()

if __name__ == '__main__':
    main()
