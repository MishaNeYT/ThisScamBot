# Если у вас не работает types, то используйте pyTelegramBotAPI!

import telebot
import random
from telebot import types

bot = telebot.TeleBot('YOU_TOKEN') # Ваш токен бота

@bot.message_handler(commands = ["start", "старт"])
def start(message):
    help_message = f'Привет <b>{message.from_user.first_name}</b>, меня зовут Афанасий Скаммер.\n\nЯ являюсь самым успешным в мире бизнесменом по продаже аккаунтов <b>PUBG, FreeFire, Call of Duty, Brawl Stars и Standoff 2</b>. Мой опыт более 10 лет, начинал с раннего возраста, и наебывал мамонтов по полной программе.\n\nХотите что нибудь купить по выгодной цене? То, рекомендую выбрать подходящую команду!'

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = types.KeyboardButton("🦣 Заскамить мамонта")
    button2 = types.KeyboardButton("🔒 Контакты")

    markup.add(button1, button2)

    bot.send_message(message.chat.id, help_message, parse_mode='html', reply_markup = markup)

@bot.message_handler(content_types = ["text"])
def bot_message(message):
    if message.chat.type == 'private':

        if message.text == '🦣 Заскамить мамонта':
            random_value = random.randint(1, 100)
            if random_value > 70:
                bot.send_message(message.chat.id, "Ураа, вы смогли заскамит мамонта, по полной программе!")
            else:
                bot.send_message(message.chat.id, "Блин, вы не смогли заскамить мамонта!")

        elif message.text == '🔒 Контакты':
            bot.send_message(message.chat.id, "Ссылка на обратную связь @FuckYouMan123")

bot.polling(none_stop = True)