import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(TOKEN)
translator = Translator()

ZODIAC_SIGNS = {
    "Овен ♈": 1,
    "Телец ♉": 2,
    "Близнецы ♊": 3,
    "Рак ♋": 4,
    "Лев ♌": 5,
    "Дева ♍": 6,
    "Весы ♎": 7,
    "Скорпион ♏": 8,
    "Стрелец ♐": 9,
    "Козерог ♑": 10,
    "Водолей ♒": 11,
    "Рыбы ♓": 12
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Овен ♈')
    item2 = types.KeyboardButton('Телец ♉')
    item3 = types.KeyboardButton('Близнецы ♊')
    item4 = types.KeyboardButton('Рак ♋')
    item5 = types.KeyboardButton('Лев ♌')
    item6 = types.KeyboardButton('Дева ♍')
    item7 = types.KeyboardButton('Весы ♎')
    item8 = types.KeyboardButton('Скорпион ♏')
    item9 = types.KeyboardButton('Стрелец ♐')
    item10 = types.KeyboardButton('Козерог ♑')
    item11 = types.KeyboardButton('Водолей ♒')
    item12 = types.KeyboardButton('Рыбы ♓')
    markup.add(item2, item1, item3, item4, item5, item6, item7, item8, item9,
               item10, item11, item12)

    bot.send_message(chat_id, 'Привет!Выбери свой знак зодиака'.format(message.from_user),reply_markup=markup)


@bot.message_handler(content_types=['text'])
def echo_message(message):
    if message.text != '🔙 Назад':
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('🔙 Назад')
        markup.add(back)

        zodiaс_sign = ZODIAC_SIGNS[message.text]
        res = requests.get(
            f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={zodiaс_sign}")
        soup = BeautifulSoup(res.content, 'html.parser')
        data = soup.find('div', attrs={'class': 'main-horoscope'})
        translation = translator.translate(data.p.text, src='en', dest='ru')

        bot.send_message(chat_id, translation.text,reply_markup=markup)
    else:
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Овен ♈')
        item2 = types.KeyboardButton('Телец ♉')
        item3 = types.KeyboardButton('Близнецы ♊')
        item4 = types.KeyboardButton('Рак ♋')
        item5 = types.KeyboardButton('Лев ♌')
        item6 = types.KeyboardButton('Дева ♍')
        item7 = types.KeyboardButton('Весы ♎')
        item8 = types.KeyboardButton('Скорпион ♏')
        item9 = types.KeyboardButton('Стрелец ♐')
        item10 = types.KeyboardButton('Козерог ♑')
        item11 = types.KeyboardButton('Водолей ♒')
        item12 = types.KeyboardButton('Рыбы ♓')
        markup.add(item2, item1, item3, item4, item5, item6, item7, item8,
                   item9,
                   item10, item11, item12)

        bot.send_message(chat_id, 'Выбери свой знак зодиака'.format(
            message.from_user), reply_markup=markup)


bot.infinity_polling()
