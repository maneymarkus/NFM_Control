from absl import logging
import multiprocessing
import pathlib
import telegram
import telegram.ext

from app import utils


CHANNEL_CHAT_ID = utils.get_env_value("NETZFREQUENZMESSUNGSKONTROLLE_CHANNEL_CHAT_ID")


class TelegramBot:
    token = utils.get_env_value("TELEGRAM_BOT_API_TOKEN")
    help_text_file = pathlib.Path("./bot_help_text.txt")

    def __init__(self, channel_chat_id: int = CHANNEL_CHAT_ID):
        """
        Initialize Telegram Bot with a channel chat id. Whenever the
        `self.post_message_to_channel()` method is called the bot will post to this given channel.

        :param channel_chat_id:
        """
        self.channel_chat_id = channel_chat_id
        self.bot = telegram.Bot(token=self.token)
        self.process = None

    def _run_bot(self, logging_level=logging.INFO):
        """
        Run the bot and listen to commands

        :param logging_level:
        :return:
        """
        logging.set_verbosity(logging_level)
        logging.info("Run telegram bot")

        # initialize bot here again because of different threads
        self.bot = telegram.Bot(token=self.token)
        application = telegram.ext.ApplicationBuilder().token(self.token).build()

        application.add_handler(telegram.ext.CommandHandler("help", self.help))

        application.run_polling()

    async def help(self, update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE) \
            -> None:
        """
        Help command handler to display help text in chat

        :param update:
        :param context:
        :return:
        """
        # standard help text for when the help_text.txt file can not be opened
        if self.help_text_file.is_file():
            with open(self.help_text_file, "r", encoding="utf-8") as file:
                help_text = file.read()
                file.close()
        else:
            help_text = "Du hast die Hilfe angefordert, aber leider ist ein Fehler aufgetreten. " \
                        "Ich kann dir leider grad die Hilfe nicht anzeigen. Bitte entschuldige " \
                        "die Umstände und versuch es später erneut."
            logging.warning(f"The help text file could not be loaded at: {self.help_text_file}")
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=help_text
        )

    async def post_message_to_channel(self, message: str) -> bool:
        """
        Post a given `message` to the channel the bot got initialized with

        :param message:
        :return:
        """
        if self.bot is None:
            raise RuntimeError("The bot is not initialized")
        async with self.bot:
            result = await self.bot.send_message(chat_id=self.channel_chat_id, text=message)
        if result is not None:
            return True
        return False

    def start_bot(self, logging_level=logging.INFO):
        """
        Start a new thread with this bot running concurrently

        :param logging_level:
        :return:
        """
        if self.process is None:
            logging.info("Start telegram bot")
            self.bot = None
            self.process = multiprocessing.Process(target=self._run_bot, args=(logging_level,))
            self.process.start()
            self.bot = telegram.Bot(token=self.token)

    def stop_bot(self):
        """
        Stop the thread running this bot concurrently (if a thread is running)

        :return:
        """
        if self.process is not None and self.process.is_alive():
            logging.info("Stop telegram bot")
            self.process.terminate()
            self.process.join()
            self.process.close()
            self.process = None
