import telebot

TOKEN = '6205631880:AAEpNUxvjiL9GY8zHyI4F0d3AEDy5CGertA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я простой и понятный чат-бот. Как тебя зовут?")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if "привет" in message.text.lower():
        bot.send_message(message.chat.id, "Привет!")
    elif "как дела" in message.text.lower():
        bot.send_message(message.chat.id, "Хорошо, спасибо! Как у тебя?")
    else:
        bot.send_message(message.chat.id, "Извини, я не понимаю твоего сообщения. Можешь повторить?")

if __name__ == "__main__":
    bot.polling(none_stop=True)
