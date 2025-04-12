import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import lxml

bot = telebot.TeleBot('7630372288:AAFnUQt4amGbLXWNVkwoPYVTRnm0goEYHQA')

@bot.message_handler(commands = ['start'])
def start(message):
    Button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    go = types.KeyboardButton('расскажи анекдот')
    Button.add(go)
    bot.send_message(message.chat.id, 'если хочешь повесилиться или развеселить друзей, то быстрей нажимай на кнопку', reply_markup=Button)



@bot.message_handler(content_types = ['text'])
def anekdot(message):
    if message.text == 'расскажи анекдот':
        link = 'https://anekdoty.ru/'
        rezult = requests.get(link).text
        Html = BeautifulSoup(rezult, 'lxml')
        block = Html.find('div',id = "main" )
        block2 = block.find_all('p')[0].text
        bot.send_message(message.chat.id,f'Анекдот: { block2}')




bot.polling(none_stop = True)
