import telebot
from bittrex import BittrexClient
from bittrex import BittrexError
from logging import getLogger

logger = getLogger(__name__)

NOTIFY_PAIR = "USD-DOGE"
bot = telebot.TeleBot("1609840643:AAHNgrwRX9mWnFjkan1nVE1STBkvXAFOmOE")
client = BittrexClient()


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот створений щоб зробить з тебе успішного "
                     "кріптотрейдера як Міша".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')
    bot.send_message(message.chat.id, "Уведи пару, курс якої хоче дізнаться (формат USD-BTC)")


@bot.message_handler(content_types=['text'])
def crypto_currency_rate(message):
    try:
        pair = "{}".format(message.text)
        current_price = client.get_last_price(pair=pair)
        bot.send_message(message.chat.id, "Курс на даний момент такий:\n {}={}".format(pair, current_price))
    except BittrexError:
        bot.send_message(message.chat.id, "Не пиши дурню (спробуй ще)")


if __name__ == "__main__":
    bot.polling(none_stop=True)
