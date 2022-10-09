import dotenv
import os
import telegram
import telegram.ext

ENV_VALUES = dotenv.dotenv_values(".env")
TELEGRAM_BOT_API_TOKEN = ENV_VALUES["TELEGRAM_BOT_API_TOKEN"]
CHANNEL_CHAT_ID = ENV_VALUES["NETZFREQUENZMESSUNGSKONTROLLE_CHANNEL_CHAT_ID"]


def post_message(message: str):
    """

    :param message:
    :return:
    """
    try:
        bot = telegram.Bot(token=TELEGRAM_BOT_API_TOKEN)
        bot.sendMessage(CHANNEL_CHAT_ID, message)
    except():
        # TODO: handle error
        pass
    return True


def start(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        rf"Hi {user.mention_markdown_v2()}\!",
        reply_markup=telegram.ForceReply(selective=True)
    )


def echo(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def inline_query(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    query = update.inline_query
    text = query.query
    print(text)
    query.from_user.send_message(text)


if __name__ == "__main__":
    #m = "Hello Channel"
    #post_message(m)
    updater = telegram.ext.Updater(TELEGRAM_BOT_API_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(telegram.ext.CommandHandler("start", start))

    #dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text & ~telegram.ext.Filters.command, echo))

    dispatcher.add_handler(telegram.ext.InlineQueryHandler(inline_query))

    updater.start_polling()

    updater.idle()
