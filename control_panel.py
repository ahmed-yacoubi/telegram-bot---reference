#!/usr/bin/env python3

import response as R

import utils as Keys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

coin_name = ''
coin_info = ''


def startCommand(update, context):
    update.message.reply_text('اهلا بك في لوحة التحكم ...')


def add_coin(update, context):
    update.message.reply_text('ادخل اسم العملة')
    coin_name = update.message.text
    update.message.reply_text('ادخل معلومات العملة ')
    coin_info = update.message.text
    print('{} , {} '.format(coin_name, coin_info))
    coin_name = ''
    coin_info = ''


def helpCommand(update, context):
    update.message.reply_text('No Helper')


def handelMessage(update, context):
    user = update.message.from_user
    text = str(update.message.text).upper()
    coin_name = text
    update.message.reply_text('ادخل معلومات العملة ')


def main():
    updater = Updater(Keys.API_BOT_KEY_CONTROL_PANEL, use_context=True)
    dis = updater.dispatcher
    dis.add_handler(CommandHandler("start", startCommand))
    dis.add_handler(CommandHandler("help", startCommand))
    dis.add_handler(CommandHandler("add_coin", add_coin))

    # dis.add_handler(MessageHandler(Filters.text, handelMessage))

    updater.start_polling()
    updater.idle()


main()
