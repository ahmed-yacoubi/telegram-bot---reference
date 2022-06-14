import response as R
import utils as Keys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print("Bot Started")
welcome_text ="اهلاً بكم جميعاً 👋🏼♥️\n"\
    "\n\n🤖في بوت مشاريع العملات الرقمية🤖"\
    "\nمن خلال هذا البوت :"\
    "\nتستطيع معرفة مشاريع العملات الرقمية 📝"\
    "\n\nفقط كل ما عليك تضع اختصار العملة 📍"\
    "\nتنوية ⚠️"\
    "\n ليست جميع العملات موجودة هنا 🗃"\
    "\n\nلكن اسعى لإضافة الكثير منها 🗳"\
    "\nأعداد أخوكم : عبدالله بن جنيّح"\
    "\nTwitter : @AMJ_BTC"

def startCommand(update, context):
    update.message.reply_text("")


def helpCommand(update, context):
    update.message.reply_text('No Helper')


def handelMessage(update, context):
    text = str(update.message.text).upper()
    response = R.inputText(text)
    update.message.reply_text(response)


def main():
    updater = Updater(Keys.API_BOT_KEY, use_context=True)
    dis = updater.dispatcher
    dis.add_handler(CommandHandler("start", startCommand))
    dis.add_handler(CommandHandler("help", startCommand))
    dis.add_handler(MessageHandler(Filters.text, handelMessage))
    updater.start_polling()
    updater.idle()


main()
