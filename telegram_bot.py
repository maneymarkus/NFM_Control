import dotenv
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


async def start(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_markdown_v2(
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


async def receive_channel_message(update: telegram.Update, context: telegram.ext.CallbackContext):
    print(update)
    msg = update.effective_message
    print(str(msg["text"]))


if __name__ == "__main__":
    #m = "Hello Channel"
    #post_message(m)
    application = telegram.ext.ApplicationBuilder().token(TELEGRAM_BOT_API_TOKEN).build()

    start_handler = telegram.ext.CommandHandler("start", start)
    application.add_handler(start_handler)

    message_handler = telegram.ext.MessageHandler(telegram.ext.filters.TEXT & telegram.ext.filters.ChatType.CHANNEL, receive_channel_message)
    application.add_handler(message_handler)

    application.run_polling()
