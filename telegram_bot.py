import dotenv
import os
import telegram

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


if __name__ == "__main__":
    m = "Hello Channel"
    post_message(m)
